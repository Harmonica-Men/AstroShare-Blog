from django.urls import path, include
from .views import FrontpageView, HomepageView


urlpatterns = [
    path('', HomepageView, name= 'homepage'),
    path('frontpage/', FrontpageView.as_view(), name= 'frontpage-blogpost')
]
