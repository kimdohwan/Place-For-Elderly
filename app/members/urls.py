from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    # path('signup/', views.signup_view, name='signup')
    path('signin/', views.signin_view, name='signin'),
    path('signout/', views.signout, name='signout'),
]