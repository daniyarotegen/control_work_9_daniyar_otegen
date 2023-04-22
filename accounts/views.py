from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, TemplateView


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'


class UserLoginView(LoginView):
    template_name = 'user_login.html'
    success_url = reverse_lazy('home')


class LogoutConfirmView(LoginRequiredMixin, TemplateView):
    template_name = 'user_logout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('home'))


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('home'))


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_register.html'
    success_url = reverse_lazy('login')
