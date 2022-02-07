from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.tlv.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.tdv.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.tuv.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.tdelv.as_view(), name='cbvdelete')
]