from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('name', 'email', 'registration', 'is_admin')
    list_filter = ('is_admin', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('name',)}),
        ('Permissões', {'fields': ('is_admin', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'groups')}
        ),
    )
    search_fields = ('email', 'name', 'registration')
    ordering = ('email',)
    filter_horizontal = ('groups',)

    def save_model(self, request, obj, form, change):
        """Ao salvar um usuário no Django Admin, gera matrícula automaticamente se for novo."""
        if not obj.registration and obj.groups.exists():
            group_name = obj.groups.first().name  # Pega o primeiro grupo do usuário
            obj.registration = obj.generate_registration_number(group_name)
        super().save_model(request, obj, form, change)

# Registrar User no Django Admin
admin.site.register(User, UserAdmin)

