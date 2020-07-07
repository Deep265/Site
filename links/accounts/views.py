from django.shortcuts import render
from django.urls import reverse_lazy
from .models import UserAccounts
from django.views.generic import CreateView
from .forms import UserFroms
# Create your views here.
class SignUp(CreateView):
    form_class = UserFroms
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


