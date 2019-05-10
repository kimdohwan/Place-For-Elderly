from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('list/', views.FacilityListView.as_view(), name='facility-list'),
    path('detail/<pk>', views.FacilityDetailView.as_view(), name='facility-detail'),
    path('search/', views.search_view, name='search'),
]
