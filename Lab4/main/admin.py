from django.contrib import admin
from main.models import Todo

@admin.register(Todo) #первый способ
class TodoAdmin(admin.ModelAdmin):
    list_display=('number','created','dueTo','action','completed')
    list_display_links=('action',)
    list_filter=('completed',)
    search_fields=('action',)

# admin.site.register(Todo,TodoAdmin) второй способ
