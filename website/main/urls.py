from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path("logout/",views.log_out, name="logout"),
    path("donations/",views.donations, name="donations"),
    path("trends/",views.trends, name="trends"),
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('transaction-success/', views.transaction_success, name='transaction_success'),

]
