from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(CreateView):
    template_name = 'members/signup.html'
    form_class = SignupForm
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

