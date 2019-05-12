from django.urls import path

from . import views

app_name = 'facilities'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('search/', views.search_view, name='search'),
    path('list/', views.facility_list, name='facility-list'),
    path('detail/<pk>', views.facility_detail, name='facility-detail'),
]
