from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("still.urls")),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('images/selfie.ico')))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'still.views.custom_404_view'
