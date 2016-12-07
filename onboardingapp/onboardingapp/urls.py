from django.conf.urls import url, include
# ...
from django.views.generic.base import TemplateView
# ...
from django.contrib import admin
from .views import Homeview

urlpatterns = [
    url(r"^$", Homeview.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),    
    url(r'^team/', include('team.urls','team')),    
    url(r'^organization/', include('organization.urls','organization')),

    # url(r'^test/$',
    #     TemplateView.as_view(
    #         template_name='test/index.html'
    #     ),
    #     name='test'),
]

# from team.urls import urlpatterns as team_urlpatterns
# urlpatterns += team_urlpatterns

