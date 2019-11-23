"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url,include
from users import views as users_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', users_views.register, name='register'),
    url(r'^login/', auth_views.login, {'template_name':'users/login.html'},name='login'),
    url(r'^logout/', auth_views.logout, {'template_name':'users/logout.html'},name='logout'),
    url(r'^profile/', users_views.profile, name='profile'),
    url(r'^',include('apps.blog_app.urls')),
    # url(r'^edit/profile/$', users_views.edit_profile, name='edit_profile'),
]
    # url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    # url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    # url(r'^change-password/$', views.change_password, name='change_password'),