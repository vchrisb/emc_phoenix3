from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.files.storage import get_storage_class
from django_resized import ResizedImageField
import uuid
import pyotp

# Create your models here.
class Badge(models.Model):
    """( description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    SecureStorage = get_storage_class(settings.SECURE_FILE_STORAGE)
    secret_key = models.CharField(max_length=16, default=pyotp.random_base32)
    image = ResizedImageField(size=[100, 100], crop=['middle', 'center'], upload_to='BadgePictures', storage=SecureStorage())
    class Meta:
        permissions = (
            ('view_badge_secret', 'Can view badge secret'),
        )
    
    def __str__(self):
        return str(self.name)

class CrawledBadge(models.Model):
    """( description)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='crawledbadges')
    badge = models.ForeignKey('Badge', on_delete=models.CASCADE, related_name='crawled')
    achieved_at = models.DateTimeField(default=timezone.now, editable=False)
    
    def __str__(self):
        return str(self.id)