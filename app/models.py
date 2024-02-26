from django.db import models
import shortuuid
from uuid import uuid1

# Create your models here.  

class Pasta(models.Model):
       id_pasta = models.UUIDField(primary_key=True, default=uuid1, editable=False)
       nome = models.CharField(max_length=20, default='New Folder')
       
       
class SubPasta(models.Model):
       id_subpasta = models.CharField(max_length=22, primary_key=True, default=shortuuid.uuid, editable=False)
       nome = models.CharField(max_length=20, default='NEW ARQUIVOS' )
       descricao = models.TextField(default='Description')
       id_pasta_pai = models.ForeignKey(Pasta, on_delete=models.CASCADE, related_name='subpastas')
       