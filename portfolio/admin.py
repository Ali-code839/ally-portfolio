# Import Django's admin module.
from django.contrib import admin

# Import the Project model that should be manageable from the admin dashboard.
from .models import Project


# Define how Project records appear inside Django admin.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Show these useful columns in the project list.
    list_display = ('title', 'category', 'created_at')
    # Add a category filter to the right side of the admin list.
    list_filter = ('category',)
    # Make project titles searchable.
    search_fields = ('title', 'description')
    # Display newest projects first.
    ordering = ('-created_at',)
