from django.urls import path
from. import views

urlpatterns = [
   
   path('', views.home, name='home'),
   path('login/', views.login, name='login'),
   path('menu/', views.menu, name='menu'),
   path('signup/', views.signup, name='signup'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('logout/', views.logout, name='logout'),
   path('bicycle/', views.bicycle, name='bicycle'),
   path('bikes/', views.bikes, name='bikes'),
   path('scooter/', views.scooter, name='scooter'),
   path('splendor/', views.splendor, name='splendor'),
   path('form/<id>', views.form, name='form'),
   path('booking/', views.booking, name='booking'),
   
    path('userlist/',views.user_list,name='user_list'),
    path('del_user/<id>',views.delete_user,name='delete_user'),
    path('edit_user/<id>',views.editUser,name="editUser"),
    path('updateUser',views.update_user,name='update_user'),
    path('order_list',views.order_list,name='order_list'),


    path('prod_detail/',views.prod_detail,name='prod_detail'),
    path('add_prod/',views.add_prod,name="add_prod"),
    path('view_details/<id>/', views.viewdetails, name='viewdetails'),

    path('delete_Product/<id>',views.deleteProd,name='deleteProd'),
    path('edit_Prod/<id>',views.editProd,name="editProd"),
    path('update_Prod',views.updateProd,name='updateProd'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
   
]