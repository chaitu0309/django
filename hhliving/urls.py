"""hhliving URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from users import urls as users_urls
from hhliving import settings
from users import views as user_views

from rest_framework import routers
from users import viewsets as users_viewsets
from habits import viewsets as habits_viewsets

router = routers.DefaultRouter()
router.register(r'users', users_viewsets.HUserViewSet)
router.register(r'edit_users', users_viewsets.HUserEditViewSet)
router.register(r'circles', users_viewsets.CircleListViewSet)
router.register(r'edit_circles', users_viewsets.CircleEditViewSet)
router.register(r'circlemembers', users_viewsets.CircleMemberListViewSet)
router.register(r'edit_circlemembers', users_viewsets.CircleMemberEditViewSet)
router.register(r'habits', habits_viewsets.HabitListViewSet)
router.register(r'habitservices', habits_viewsets.HabitServiceListViewSet)
router.register(r'edit_habitservices', habits_viewsets.HabitServiceUpdateViewSet)
router.register(r'circlemembers', habits_viewsets.HabitReviewListViewSet)

#router.register(r'^edit_users/(?P<pk>[0-9]+)$/edit_circles/(?P<pk>[0-9]+)$', users_viewsets.CircleMemberViewSet)

urlpatterns = [
    url(r'^$', user_views.index, name='index'),
    url(r'^users/', include(users_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)