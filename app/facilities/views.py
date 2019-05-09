from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from facilities.models import Facility


class FacilityListView(ListView):
    model = Facility
    # 모두 Default 설정 값과 동일
    template_name = 'facilities/facility_list'
    context_object_name = 'facility_list'
    queryset = Facility.objects.all()


def search_view(request):
    qs = None
    q = request.GET.get('q', '')
    if q:
        qs = Facility.objects.filter(Q(REFINE_LOTNO_ADDR__icontains=q) | Q(REFINE_ROADNM_ADDR__icontains=q)).order_by('SIGUN_CD')  # 시/군 필터링

    return render(request, 'facilities/search_view.html', {
        'facility_list': qs,
        'q': q,
    })
