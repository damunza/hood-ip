from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/(\w+)', views.profile, name='profile'),
    url(r'^add/(?P<operation>.+)/(?P<name>\w+)', views.new_resident, name='new_being'),
    url(r'^area/(\w+)', views.residence, name='area'),
    url(r'^business/(\w+)', views.new_business, name='bizna'),
    url(r'^service/(\w+)', views.new_service, name='service'),
    url(r'^event/(\w+)', views.new_event, name='event'),
    url(r'^newhood$', views.new_hood, name='esto'),
    url(r'^search/', views.search, name='search'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
