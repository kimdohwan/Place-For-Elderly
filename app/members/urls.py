from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('info/<pk>/', views.user_info, name='userinfo'),
    path('like/<pk>', views.like_facility, name='like-facility')
]
