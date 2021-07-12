from django.conf.urls import url
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.
urlpatterns = [url(r"^profile/([\w\-]+)", views.profile, name="profile")]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
