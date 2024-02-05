from django.contrib import admin
from .models import Post


# Use specific model - Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # Set essential fields
    list_filter = ['status', 'created', 'publish', 'author']  # Allows set right-side menu for searching
    search_fields = ['title', 'body']  # Add search field
    prepopulated_fields = {'slug': ('title',)}  # Set to automatic filling of slug field in the add-post-window
    raw_id_fields = ['author']  # Use for many-users apps, change to choice of author(search widget)
    date_hierarchy = 'publish'  # Add to panel of navigations
    ordering = ['status', 'publish']  # Set to sorting criteria
