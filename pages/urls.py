from django.urls import path
from .views import *

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('about/', AboutPageView.as_view(), name='aboutpage'),
]
