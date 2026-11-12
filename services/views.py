# Import Django's render shortcut.
from django.shortcuts import render


# Display the services offered through the portfolio.
def services_list(request):
    # Keep the service descriptions in one easy-to-edit list for this small portfolio.
    services = [
        {'number': '01', 'title': 'Graphic Design', 'description': 'Logos, brand identities, posters, social media graphics and polished marketing materials.'},
        {'number': '02', 'title': 'Photography', 'description': 'Portraits, events, products and visual storytelling designed for memorable presentation.'},
        {'number': '03', 'title': 'Videography', 'description': 'Short-form content, event coverage, promotional videos and clean video editing.'},
        {'number': '04', 'title': 'Web Development', 'description': 'Modern responsive websites and web applications built with Django and practical UI design.'},
        {'number': '05', 'title': 'IT Consulting', 'description': 'Technical guidance, computer support, networking and digital solutions for teams and businesses.'},
    ]

    # Render the services page with the service list.
    return render(request, 'services.html', {'services': services})
