from django.shortcuts import render
from services import models

def dashboard(request):
    chamado_atual = models.Agendamento.objects.filter(status=False).order_by('-data_agendamento', '-hora').first()
    ultimas_chamadas = models.Agendamento.objects.filter(status=False).order_by('-data_agendamento', '-hora')[:5]
    emergencia = models.Prontuario.objects.filter(urgencia='EMERGENCIA', agendamento__status=False).count()
    muito_urgente = models.Prontuario.objects.filter(urgencia='MUITO URGENTE', agendamento__status=False).count()
    urgente = models.Prontuario.objects.filter(urgencia='URGENTE', agendamento__status=False).count()
    pouco_urgente = models.Prontuario.objects.filter(urgencia='POUCO URGENTE', agendamento__status=False).count()
    nao_urgente = models.Prontuario.objects.filter(urgencia='NÃO URGENTE', agendamento__status=False).count()

    context={
        'chamado_atual': chamado_atual,
        'ultimas_chamadas': ultimas_chamadas,
        'emergencia':emergencia,
        'muito_urgente': muito_urgente,
        'urgente': urgente,
        'pouco_urgente': pouco_urgente,
        'nao_urgente': nao_urgente
    }

    return render(request, 'dashboard.html', context=context)
