import random
import string
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, group_name=None, **extra_fields):
        """Cria um usuário normal, gera matrícula e associa a um grupo."""
        if not email:
            raise ValueError("O usuário deve ter um e-mail válido")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)

        # 🔹 Agora a matrícula volta a ser gerada automaticamente!
        if group_name:
            group, _ = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            user.registration = user.generate_registration_number(group_name)
            user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password, **extra_fields):
        """Cria um superusuário manualmente (sem geração automática de matrícula)."""
        extra_fields.pop('registration', None)  # Remove 'registration' caso o Django tente passar
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
    registration = models.CharField(max_length=8, unique=True)  # 🔹 Voltamos a exigir matrícula
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'registration'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return f"{self.name} ({self.registration})"

    @property
    def is_staff(self):
        return self.is_admin

    def generate_registration_number(self, group_name):
        """Gera um número de matrícula único baseado no grupo ('M' para médicos, 'F' para funcionários)."""
        prefix = "M" if group_name == "Médico" else "F" if group_name == "Funcionário" else "U"
        while True:
            random_number = ''.join(random.choices(string.digits, k=7))
            registration_number = f"{prefix}{random_number}"
            if not User.objects.filter(registration=registration_number).exists():
                return registration_number
