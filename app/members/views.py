from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DetailView

from facilities.models import Facility
from .models import User, LikeFacility
from .forms import SignupForm, SigninForm


# class SignupView(CreateView):
#     template_name = 'members/signup.html'
#     form_class = SignupForm
#     # 회원가입 성공시 이동시킬 페이지
#     success_url = reverse_lazy('facilities:index')
#
#     def post(self, request, *args, **kwargs):
#         self.object = None
#         return super().post(request, *args, **kwargs)

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('facilities:index')
    else:
        form = SignupForm()
    return render(request, 'members/signup.html', {'form': form})


def signin_view(request):
    form = SigninForm(data=request.POST)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('facilities:index')
    else:
        form = SigninForm()

    context = {
        'form': form,
    }
    return render(request, 'members/signin.html', context)


def signout(request):
    logout(request)
    return redirect('facilities:index')


class UserInfoView(DetailView):
    model = User
    # 모두 Default 설정 값과 동일
    template_name = 'members/member_detail.html'
    context_object_name = 'member'


@require_POST
def like_facility(request, pk):
    if request.user.is_authenticated:
        user = request.user
        facility = Facility.objects.get(pk=pk)

        if facility not in user.facility_list:
            like = LikeFacility(user=user, facility=facility)
            like.save()
            messages.add_message(request, messages.INFO, '관심목록 추가에 추가되었습니다.')
        else:
            messages.add_message(request, messages.INFO, '이미 추가된 시설입니다.')

        current_page = request.META.get("HTTP_REFERER")
        return HttpResponseRedirect(current_page)
    else:
        return redirect('members:signin')


# signup = SignupView.as_view()
user_info = UserInfoView.as_view()
