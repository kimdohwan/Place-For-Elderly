from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.fac_list, name='facility-list'),
    path('detail/<pk>', views.fac_detail, name='facility-detail'),
    path('', views.index_view, name='index'),
    path('search/', views.search_view, name='search'),
]
