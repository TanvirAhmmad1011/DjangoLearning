from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('signin/',views.SignIn.as_view(),name='signin'),
    path('signout/',views.signout,name='signout')
]