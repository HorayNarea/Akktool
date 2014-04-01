from django.shortcuts import render
from akkreditierung.models import Member


def quorum(request):
    basis = len(Member.objects.filter(haspaid=1))
    akk = len(Member.objects.filter(akk=1))
    quorum = float(akk) / float(basis) * 100
    context = {'basis': basis, 'akk': akk, 'quorum': quorum}
    return render(request, 'akkreditierung/quorum.html', context)
