from django.urls import path
from .views import MainPage, Detail, Create, Update, Delete

urlpatterns = [
    path('',MainPage.as_view(), name='main'),
    path('blog/create', Create.as_view(), name= 'create'),
    path('blog/<slug:slug>/update', Update.as_view(), name='update'),
    path('blog/<slug:slug>', Detail.as_view(), name='detail'),
    path('blog/<slug:slug>/delete', Delete.as_view(), name='delete')
    
]
