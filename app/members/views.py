from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm, SigninForm


class SignupView(CreateView):
    template_name = 'members/signup.html'
    form_class = SignupForm
    # 회원가입 성공시 이동시킬 페이지
    success_url = reverse_lazy('index')

    # def signup_view(request):
    #     if request.method == 'POST':
    #         form = SignupForm(request.POST)
    #     else:
    #         form = SignupForm()
    #
    #     context = {
    #         'form': form,
    #     }
    #     return render(request, 'members/signup.html', context)


def signin_view(request):
    form = SigninForm(data=request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form.error = form.error_messages['invalid_login']
            # return redirect('signin')
    else:
        form = SigninForm()

    context = {'form': form}
    return render(request, 'members/signin.html', context)


def signout(request):
    logout(request)
    return redirect('index')
