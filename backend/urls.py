from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from xmas import views

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('GuestBook', views.GuestBookView, 'GuestBook')
router.register('HostPost', views.HostPostView, 'HostPost')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)