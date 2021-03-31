from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuditModel(models.Model):
    # Audit Fields
    create_on = models.DateTimeField('Criado em', auto_now_add=True)
    updated_on = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract=True


class Usuario(AbstractUser,AuditModel):
    username = None
    email = models.EmailField("Email", unique=True)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=16)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.nome_completo

    def primeiro_nome(self):
        return self.nome_completo.split()[0]