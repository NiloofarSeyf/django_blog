from django.contrib import admin
from .models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_time_modified',)
    ordering = ('-status', )


# admin.site.register(Post, PostAdmin)
