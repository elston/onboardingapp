from django.conf.urls import url, include
# ...
from django.contrib import admin
from .views import Homeview

urlpatterns = [
    url(r"^$", Homeview.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),    
]
