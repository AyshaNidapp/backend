from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_parent, name='add_parent'),
    path('get/<int:pk>/', views.get_parent, name='get_parent'),
    path('update/<int:pk>/', views.update_parent, name='update_parent'),
    path('delete/<int:pk>/', views.delete_parent, name='delete_parent'),
    path('signup/', views.signup_parent, name='signup_parent'),
    path('login/', views.login_parent, name='login_parent'),
]


