from django.db import models
from uuid import uuid1

# Create your models here.

class Pasta(models.Model):
       id_pasta = models.UUIDField(primary_key=True, default=uuid1, editable=False)
       nome = models.CharField(max_length=20)
       
       
class SubPasta(models.Model):
       id_subpasta = models.UUIDField(primary_key = True, default=uuid1, editable=False)
       nome = models.CharField(max_length=20)
       descricao = models.TextField()
       pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE, related_name='subpastas')
       
       