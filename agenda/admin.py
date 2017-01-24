from django.contrib import admin
from .models import Entry, EntryGroup, EntryLocation
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ["title", "start", "end", "publish"]
    ordering = ['start']

class EntryGroupAdmin(admin.ModelAdmin):
    list_display = ["groupname"]

class EntryLocationAdmin(admin.ModelAdmin):
    list_display = ["locationname"]
    
admin.site.register(EntryGroup,EntryGroupAdmin)   
admin.site.register(Entry,EntryAdmin)
admin.site.register(EntryLocation,EntryLocationAdmin)