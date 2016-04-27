from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from .views import register, registration_complete

app_name = 'base'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    # Registration URLs
    url(r'^register/$', register, name='register'),
    url(r'^register/complete/$', registration_complete,
        name='registration_complete'),
] + staticfiles_urlpatterns()
