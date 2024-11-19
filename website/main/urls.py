from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path("logout/",views.log_out, name="logout"),
    path("donations/",views.donations, name="donations"),
    path("trends/",views.trends, name="trends"),
    
  
    path('general-transactions/', views.view_general_transactions, name='view_general_transactions'),
    path('add-general-transaction/', views.add_general_transaction, name='add_general_transaction'),
    path('create-project/', views.create_project, name='create_project'),
    path('project-transactions/<int:project_id>/', views.view_project_transactions, name='view_project_transactions'),
    path('add-project-transaction/<int:project_id>/', views.add_project_transaction, name='add_project_transaction'),
    path('edit-project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('archive-project/<int:project_id>/', views.archive_project, name='archive_project'),
    path('archived-projects/', views.archived_projects, name='archived_projects'),
    path('restore-project/<int:project_id>/', views.restore_project, name='restore_project'),



]
