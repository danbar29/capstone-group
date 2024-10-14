# map urls to view function

from django.urls import path
from . import views

# url configuration
urlpatterns = [
    path('hello/',views.say_hello),

    path('second/',views.second_exp)

]