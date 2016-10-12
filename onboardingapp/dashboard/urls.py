from django.conf.urls import url
from .views import index
from .router import router
api = router.api

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/$', api, name='api'),               
    url(r'^router/$', router, name='router'),        
]


