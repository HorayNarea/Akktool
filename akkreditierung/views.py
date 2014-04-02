from django.shortcuts import render
from akkreditierung.models import Member


def quorum(request):
    mitglieder = len(Member.objects.all())
    basis = len(Member.objects.filter(haspaid=1))
    akk = len(Member.objects.filter(akk=1))
    bezahlt = float(basis) / float(mitglieder) * 100
    quorum = float(akk) / float(basis) * 100
    context = { 'basis': basis, 'akk': akk, 'quorum': round(quorum, 1), 'mitglieder': mitglieder , 'bezahlt': round(bezahlt, 1) }
    return render(request, 'akkreditierung/quorum.html', context)
