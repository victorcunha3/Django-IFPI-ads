from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

NIVEL_CHOICES = [
    (1,1),
    (3,3),
    (5,5),
    (8,8),
]

PRIORIDADE_CHOICES =[
    (1,1),
    (2,2),
    (3,3),
]

SITUACAO_CHOICES = [
    ('nova', 'nova'),
    ('em andamento', 'em andamento'),
    ('pendente', 'pendente'),
    ('resolvido', 'resolvido')
]

User = get_user_model()

class Tarefas(models.Model):
    descricao = models.CharField(max_length=300)
    responsavel = models.CharField(max_length=70)
    situacao = models.CharField(choices=SITUACAO_CHOICES)
    nivel = models.PositiveIntegerField(validators=[MinValueValidator(limit_value=1)], choices=NIVEL_CHOICES)
    prioridade = models.PositiveIntegerField(validators=[MinValueValidator(limit_value=1)], choices=PRIORIDADE_CHOICES)
    usuario = models.ForeignKey(User, related_name='tarefas', on_delete=models.SET_NULL, null=True, default=None)