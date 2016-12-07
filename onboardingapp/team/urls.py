from django.conf.urls import url
from team import views
# ...
urlpatterns = [

    url(r'^$',  
        views.Teams.as_view(), 
            name='index'),

    url(r'^update/(?P<id>\d+)$',  
        views.TeamUpdate.as_view(), 
            name='update'),    
]


# ...
from .router import router
api = router.api
urlpatterns = urlpatterns + [
    url(r'^api/$', api, name='api'),               
    url(r'^router/$', router, name='router'),    
]