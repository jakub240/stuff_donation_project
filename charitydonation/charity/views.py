from django.shortcuts import render
from django.views import View

# Create your views here.

class Landing_Page(View):
    def get(self, request):        
        return render(request, 'index.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')




