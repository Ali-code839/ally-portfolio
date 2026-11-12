# Import Django's render shortcut for returning HTML templates.
from django.shortcuts import render

# Import the Project database model.
from .models import Project


# Display the portfolio and optionally filter it by category.
def portfolio_list(request):
    # Read the category from the URL query string, for example ?c=photo.
    category = request.GET.get('c', 'all')

    # Start with every project, newest projects first.
    projects = Project.objects.all().order_by('-created_at', '-id')

    # Filter the database query when a valid category was requested.
    if category in {'graphic', 'photo', 'video', 'web'}:
        projects = projects.filter(category=category)

    # Render the portfolio template and pass the projects and selected filter to it.
    return render(request, 'portfolio.html', {'projects': projects, 'active_category': category})
