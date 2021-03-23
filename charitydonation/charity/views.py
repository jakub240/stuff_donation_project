from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Category, Institution, Donation
from django.db.models import Sum
from .func.landing_page import dyna_stats, institution
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# class LoginView(View):
#     def get(self, request):
#
#         return render(request, 'registration/login.html')
#
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             next_url = request.GET.get('next')
#             return redirect(next_url or 'landing-page')
#         return redirect('register')
#
#
# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('landing-page')


class LandingPage(View):
    def get(self, request):
        dyna_stats()
        institution()

        return render(request, 'index.html', institution() and dyna_stats())


class Register(View):
    def get(self, request):
        return render(request, 'register.html')


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')




