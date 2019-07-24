
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('count/',views.count),
    path('about/',views.about)
]
