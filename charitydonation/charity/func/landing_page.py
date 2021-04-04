from ..models import Category, Institution, Donation, User
from django.db.models import Sum


def dyna_stats():
    donations = Donation.objects.all()
    quantity_sum = donations.aggregate(Sum('quantity'))['quantity__sum']
    inst_in_dnt_lst = []
    context = {
        'quantity_sum': quantity_sum,
    }

    if donations:
        for dnt in donations:
            inst_in_dnt = dnt.institution
            inst_in_dnt_lst.append(inst_in_dnt)

        inst_set = set(inst_in_dnt_lst)
        inst_lst = list(inst_set)
        inst_count = len(inst_lst)

        context['inst_count'] = inst_count
        return context


def institution():
    inst_fn = Institution.objects.filter(type='FN')
    inst_op = Institution.objects.filter(type='OP')
    inst_zl = Institution.objects.filter(type='ZL')
    context = {
        "inst_fn": inst_fn,
        "inst_op": inst_op,
        "inst_zl": inst_zl,
    }
    return context
