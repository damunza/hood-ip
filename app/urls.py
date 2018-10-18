from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^profile/(\w+)', views.profile, name='profile'),
    url(r'^add/(?P<operation>.+)/(?P<name>\w+)', views.new_resident, name='new_being'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
