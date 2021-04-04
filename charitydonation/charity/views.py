from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy, reverse
from .models import Category, Institution, Donation
from .func.landing_page import dyna_stats, institution
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import RegisterForm, DonationForm, NewLoginForm, UserSettingsForm
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.forms import AuthenticationForm


class LandingPage(View):
    def get(self, request):
        dyna_stats_result = dyna_stats()
        inst_result = institution()
        dyna_stats_result.update(inst_result)

        return render(request, 'index.html', dyna_stats_result)


class CustomLogin(View):
    def get(self, request):
        form = NewLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = NewLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                return redirect('register')
            else:
                login(request, user=user)
                return redirect('landing-page')

        return render(request, 'login.html', {'form': form})


class Register(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login/'

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
            return redirect('form-confirmation')


class FormConfirmation(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


class UserProfile(View):
    def get(self, request):
        user = request.user
        user_donations = Donation.objects.filter(user=user)
        context = {
            'user': user,
            'donations': user_donations,
        }
        return render(request, 'registration/profile.html', context)


class UserSettings(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('landing-page')
