from django.urls import path, include
from .views import views

urlpatterns = [
    path('', HomePageView.as_view(), name= 'frontpage'),
]
