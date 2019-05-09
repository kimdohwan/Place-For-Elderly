from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.FacilityListView.as_view(), name='facility-list'),
    path('search/', views.search_view, name='search')
]
