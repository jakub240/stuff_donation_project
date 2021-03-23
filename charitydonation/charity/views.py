from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Category, Institution, Donation
from .func.landing_page import dyna_stats, institution
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView


class LandingPage(View):
    def get(self, request):
        dyna_stats_result = dyna_stats()
        inst_result = institution()
        dyna_stats_result.update(inst_result)

        return render(request, 'index.html', dyna_stats_result)


class Register(View):
    def get(self, request):
        return render(request, 'register.html')


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')




