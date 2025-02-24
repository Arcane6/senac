from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, group_name=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um e-mail válido")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)

        if group_name:
            group, _ = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

        return user

    def create_superuser(self, email, name, password, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            is_admin=True,
            is_superuser=True,
            is_active=True,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin

class Paciente(models.Model):
    SEXO_CHOICES = [('M', 'M'),('F', 'F'),('O', 'O')]

    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=50) # CPF
    urgencia = models.CharField(max_length=50)
    naturalidade = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=255, null=True, blank=True) # Se menor de idade ou incapaz
    carteirinha = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES)
    cep = models.CharField(max_length=20)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pressao = models.CharField(max_length=20, null=True, blank=True)
    oxigenacao = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    uso_medicamentos = models.BooleanField()
    descricao_medicamentos = models.TextField(null=True, blank=True)
    alergias = models.BooleanField()
    descricao_alergias = models.TextField(null=True, blank=True)
    sintomas = models.TextField()

    def __str__(self):
        return f'Prontuário de {self.paciente.nome}'

class Prescricao(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return f'Prescrição de {self.prontuario.paciente.nome}'

class Diagnostico(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return f'Diagnóstico de {self.prontuario.paciente.nome}'

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_agendamento = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('medico', 'data_agendamento', 'hora')

    def __str__(self):
        return f'Agendamento de {self.paciente.nome} com {self.medico.nome} em {self.data_agendamento} às {self.hora}'

class Exame(models.Model):
    nome = models.CharField(max_length=150)
    def __str__(self):
        return self.nome

class Requisicao(models.Model):
    prontuario = models.ForeignKey('Prontuario', on_delete=models.CASCADE)
    exames = models.ManyToManyField('Exame')
    descricao = models.TextField()

    def __str__(self):
        return f'Requisição de {self.prontuario.paciente.nome} com {self.exames.count()} exame(s)'
