from django.contrib import admin
from .models import To_doModel

admin.site.register(To_doModel)

class ToDoModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'startDate','endDate', 'modifiedAt')
    date_hierarchy = 'modifiedAt'
    search_fields = ('title', 'startDate', 'endDate')
