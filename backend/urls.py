from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from xmas import views

router = routers.DefaultRouter()
router.register('GuestBook', views.GuestBookView, 'GuestBook')
router.register('HostPost', views.HostPostView, 'HostPost')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
