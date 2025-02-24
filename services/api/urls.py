# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pacientes', views.PacienteViewSet)
router.register(r'prontuarios', views.ProntuarioViewSet)
router.register(r'prescricoes', views.PrescricaoViewSet)
router.register(r'diagnosticos', views.DiagnosticoViewSet)
router.register(r'especialidades', views.EspecialidadeViewSet)
router.register(r'medicos', views.MedicoViewSet)
router.register(r'agendamentos', views.AgendamentoViewSet)
router.register(r'exames', views.ExameViewSet)
router.register(r'requisicoes', views.RequisicaoViewSet)

