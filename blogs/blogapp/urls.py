from django.urls import path
from .views import MainPage, Detail

urlpatterns = [
    path('',MainPage.as_view(), name='main'),
    path('blog/<slug:slug>', Detail.as_view(), name='detail')
]
