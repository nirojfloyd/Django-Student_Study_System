from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('youtube',views.youtube,name="youtube"),
    path('notes/',views.notes,name='notes'),
]