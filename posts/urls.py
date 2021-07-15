from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url("", views.index, name="index"),
    url(r"^post/(?P<pk>\d+)", views.view_post, name="view_post"),
    url("search/", views.search_results, name="search_results"),
    url(r"new-comment/(?P<post_id>\d+)", views.new_comment, name="new_comment"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
