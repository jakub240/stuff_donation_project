from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Category, Institution, Donation
from .func.landing_page import dyna_stats, institution
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DonationForm


class LandingPage(View):
    def get(self, request):
        dyna_stats_result = dyna_stats()
        inst_result = institution()
        dyna_stats_result.update(inst_result)

        return render(request, 'index.html', dyna_stats_result)


class Register(View):
    def get(self, request):
        return render(request, 'register.html')


class AddDonation(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        form = DonationForm
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'institutions': institutions,
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = DonationForm(request.POST)
        user = request.user
        if form.is_valid():
            Donation.objects.create(
                quantity=form.cleaned_data['quantity'],
                categories=form.cleaned_data['category'],
                institution=form.cleaned_data['institution'],
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number'],
                city=form.cleaned_data['city'],
                zip_code=form.cleaned_data['zip_code'],
                pick_up_date=form.cleaned_data['pick_up_date'],
                pick_up_time=form.cleaned_data['pick_up_time'],
                pick_up_comment=form.cleaned_data['pick_up_comment'],
                user=user
            )




