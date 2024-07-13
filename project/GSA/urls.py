from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('add_task/',views.add_task,name='add_task'),
    path('view_all_task',views.view_all_task,name='view_all_task'),
    path('my_task/',views.my_task,name='my_task'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('my_profie/',views.my_profie,name='my_profile'),
    path('delete_account/<int:pk>',views.delete_account,name='delete_account'),
    path('delete/<int:pk>',views.delete,name='delete')
]