from django.contrib import admin
from .models import Publication
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'updated')  # list of columns to display
    list_filter = ( 'author','date', 'updated')  # filter by date
    search_fields = ('title', 'body','author_username')  # search fields
    ordering = ['-date']  # sort by date
    #prepopulated_fields = {'slug': ('title',)}  # prepopulate slug field with title
# Register your models here.
admin.site.register(Publication, PublicationAdmin)

