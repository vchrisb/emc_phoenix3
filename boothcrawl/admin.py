from django.contrib import admin
from .models import Badge, CrawledBadge
from guardian.admin import GuardedModelAdmin

# Register your models here.
class BadgeAdmin(GuardedModelAdmin):
    list_display = ["name"]
    readonly_fields = ('secret_key',)

class CrawledBadgeAdmin(admin.ModelAdmin):
    list_display = ["user", "badge", "achieved_at"]
    ordering = ['achieved_at']
    
admin.site.register(Badge,BadgeAdmin)
admin.site.register(CrawledBadge,CrawledBadgeAdmin)