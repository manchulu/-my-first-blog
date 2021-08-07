from django.urls import path
from . import views

#Url patterns
urlpatterns = [
    path('', views.post_list, name='post_list')
]