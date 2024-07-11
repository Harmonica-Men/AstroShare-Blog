from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blogger.urls)),
    path('members/', include('django.contrib.auth.url')),
    path('members/', include('members.urls')),
]
  