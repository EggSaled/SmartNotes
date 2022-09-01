from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
    #list_display is what field gets displayed as a replacement for <{Object name} (x)>
    list_display = ('title',)
    #list_display will now show in the admin: {Title of Note}

admin.site.register(models.Notes, NotesAdmin)