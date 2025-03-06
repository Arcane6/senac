from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Paciente, Prontuario, Prescricao, Diagnostico, Especialidade, Medico, Agendamento, Exame, Requisicao

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('name', 'email', 'is_admin')
    list_filter = ('is_admin', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('name',)}),
        ('Permissões', {'fields': ('is_admin', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'groups', )}
        ),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ('groups', )

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'documento', 'telefone', 'email', 'cidade', 'estado')
    search_fields = ('nome', 'documento', 'email', 'telefone')
    list_filter = ('cidade', 'estado')

@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'temperatura', 'pressao', 'oxigenacao', 'peso', 'uso_medicamentos', 'alergias', 'data_criacao')
    search_fields = ('paciente__nome',)
    list_filter = ('uso_medicamentos', 'alergias')

@admin.register(Prescricao)
class PrescricaoAdmin(admin.ModelAdmin):
    list_display = ('prontuario', 'descricao')
    search_fields = ('prontuario__paciente__nome',)

@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('prontuario', 'descricao')
    search_fields = ('prontuario__paciente__nome',)

@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especialidade', 'telefone', 'email', 'cidade')
    search_fields = ('nome', 'crm', 'especialidade__nome')
    list_filter = ('especialidade', 'cidade')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data_agendamento', 'hora', 'observacoes')
    search_fields = ('paciente__nome', 'medico__nome')
    list_filter = ('data_agendamento', 'medico')

@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Requisicao)
class RequisicaoAdmin(admin.ModelAdmin):
    list_display = ('prontuario', 'descricao')
    search_fields = ('prontuario__paciente__nome',)
    filter_horizontal = ('exames',)  # Para facilitar a seleção de múltiplos exames






