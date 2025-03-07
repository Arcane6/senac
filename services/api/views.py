# views.py
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.admin.models import LogEntry, CHANGE, ADDITION, DELETION
from ..models import Paciente, Prontuario, Prescricao, Diagnostico, Especialidade, Medico, Agendamento, Exame, Requisicao
from . import serializers



# def log_action(request, obj, action_flag, message):
#     """Registra a ação no LogEntry."""
#     user = request.user if request and request.user.is_authenticated else None
#     LogEntry.objects.log_action(
#         user_id=user.id if user else None,
#         content_type_id=None,
#         object_id=obj.id,
#         object_repr=str(obj),
#         action_flag=action_flag,
#         change_message=message
#     )


class BaseViewSet(viewsets.ModelViewSet):
    """Base ViewSet para adicionar registro de LogEntry em cada ação."""
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     log_action(self.request, instance, ADDITION, 'Objeto criado.')

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     log_action(self.request, instance, CHANGE, 'Objeto atualizado.')

    # def perform_destroy(self, instance):
    #     log_action(self.request, instance, DELETION, 'Objeto excluído.')
    #     instance.delete()


class PacienteViewSet(BaseViewSet):
    queryset = Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer


class ProntuarioViewSet(BaseViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = serializers.ProntuarioSerializer


class PrescricaoViewSet(BaseViewSet):
    queryset = Prescricao.objects.all()
    serializer_class = serializers.PrescricaoSerializer


class DiagnosticoViewSet(BaseViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = serializers.DiagnosticoSerializer


class EspecialidadeViewSet(BaseViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = serializers.EspecialidadeSerializer


class MedicoViewSet(BaseViewSet):
    queryset = Medico.objects.all()
    serializer_class = serializers.MedicoSerializer


class AgendamentoViewSet(BaseViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = serializers.AgendamentoSerializer


class ExameViewSet(BaseViewSet):
    queryset = Exame.objects.all()
    serializer_class = serializers.ExameSerializer


class RequisicaoViewSet(BaseViewSet):
    queryset = Requisicao.objects.all()
    serializer_class = serializers.RequisicaoSerializer
