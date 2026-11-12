# Import Django's admin site so the portfolio can be managed from /admin/.
from django.contrib import admin

# Import URL helpers used to connect each application to the project.
from django.urls import include, path

# Import settings so media files can be served during local development.
from django.conf import settings

# Import Django's helper for serving development media files.
from django.conf.urls.static import static

# Define the top-level URL routes for the entire project.
urlpatterns = [
    # Send /admin/ requests to Django's administration panel.
    path('admin/', admin.site.urls),
    # Send the homepage and contact page to the main application.
    path('', include('main.urls')),
    # Send portfolio requests to the portfolio application.
    path('portfolio/', include('portfolio.urls')),
    # Send service requests to the services application.
    path('services/', include('services.urls')),
]

# Serve uploaded images from MEDIA_ROOT while DEBUG is enabled.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
