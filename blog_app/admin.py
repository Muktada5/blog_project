from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date') # Fields to display in the admin list view
    search_fields = ('title', 'author') # Enable search by title and author
    list_filter = ('published_date', 'author') # Filter posts by date and author
    ordering = ('-published_date',) # Display latest posts first
    prepopulated_fields = {'title': ('title',)} # Prepopulate fields if needed
