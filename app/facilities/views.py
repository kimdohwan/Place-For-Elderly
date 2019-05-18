from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Facility


class FacilityListView(ListView):
    model = Facility
    # 모두 Default 설정 값과 동일
    template_name = 'facilities/facility_list.html'
    context_object_name = 'facility_list'
    queryset = Facility.objects.all()


class FacilityDetailView(DetailView):
    model = Facility
    # 모두 Default 설정 값과 동일
    template_name = 'facilities/facility_detail.html'
    context_object_name = 'facility'


def index_view(request):
    return redirect('facilities:facility-list')


def search_view(request):
    query_set = Facility.objects.none()

    search_text = request.GET.get('search_text', None)
    search_option = request.GET.get('search_option', 'address')
    if search_option == 'facility_address':
        query_set = Facility.objects.filter(
            Q(REFINE_LOTNO_ADDR__icontains=search_text) |
            Q(REFINE_ROADNM_ADDR__icontains=search_text)).order_by(
            'SIGUN_CD'
        )
    elif search_option == 'facility_name':
        query_set = Facility.objects.filter(BIZPLC_NM__icontains=search_text)

    context = {
        'facility_list': query_set,
        'search_text': search_text,
    }
    return render(request, 'facilities/facility_list.html', context)


facility_list = FacilityListView.as_view()
facility_detail = FacilityDetailView.as_view()
