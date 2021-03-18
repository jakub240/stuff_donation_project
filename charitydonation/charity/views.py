from django.shortcuts import render
from django.views import View
from .models import Category, Institution, Donation
from django.db.models import Sum



class Landing_Page(View):
    def get(self, request):
        
        works = Donation.objects.all()
        works_sum = works.aggregate(Sum('quantity'))['quantity__sum']
        institutions = Institution.objects.all()
        inst_in_dnt_lst = []        

        if works:
            for dnt in works:
                inst_in_dnt = dnt.institution
                inst_in_dnt_lst.append(inst_in_dnt)            
                        
            inst_set = set(inst_in_dnt_lst)
            inst_lst = list(inst_set)
            inst_count = len(inst_lst)         

        context = {
            'works_sum': works_sum,
            'inst_count': inst_count,
        }

        return render(request, 'index.html', context)


class Register(View):
    def get(self, request):
        return render(request, 'register.html')


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')




