from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_category', 'post_published_date', 'post_slug')

admin.site.register(Post, PostAdmin)