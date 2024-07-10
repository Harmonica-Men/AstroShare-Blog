from django.urls import path, include
from .views import FrontpageView


urlpatterns = [
    # path('', HomePageView.as_view(), name= 'homepage'),
    path('', FrontpageView.as_view(), name= 'frontpage-blogpost')
]
