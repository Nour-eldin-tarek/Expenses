from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='blog'),
    path('bill', views.bill, name='blog'),
    path('view', views.view, name='blog'),
        ]