from django.db import models
from django.utils import timezone
import datetime
import uuid
# Create your models here.

class EntryGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groupname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.groupname)

class EntryLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    locationname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.locationname)
        
class Entry(models.Model):
    """( description)"""
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    speaker = models.CharField(max_length=100, blank=True, default='')
    publish = models.BooleanField(default=False)
    entrygroup = models.ForeignKey(EntryGroup, related_name='group', blank=True, verbose_name="Group", null=True)
    entrylocation = models.ForeignKey(EntryLocation, related_name='location', blank=True, verbose_name="Location", null=True)

    def __str__(self):
        return str(self.title)

    def get_duration(self):
        timedelta = self.end - self.start
        timedelta = int(timedelta.seconds / 60)
        return timedelta

    def is_happening(self):
            """Return True if the event is happening 'now', False if not."""
            now = timezone.now()
            start = self.start
            end = self.end
            happening = False
            # check that the event has started and 'now' is btwn start & end:
            if (now >= start) and (start <= now <= end):
                happening = True
            return happening
