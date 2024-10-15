from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path("logout/",views.log_out, name="logout"),
    path("donations/",views.donations, name="donations"),
    path("trends/",views.trends, name="trends"),
]