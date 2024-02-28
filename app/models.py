from django.db import models
from django.core.exceptions import ValidationError
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

class BoardApp(models.Model):
    id_board_app = models.CharField(max_length=22, primary_key=True, default=shortuuid.uuid, editable=False)
    url_youtube = models.CharField(max_length=100, blank=True, null=True)
    anotacoes = models.TextField(default='anotacoes', blank=True, null=True)
    transcricao = models.TextField(default='transcricao', blank=True, null=True)
    resumo = models.TextField(default='resumo', blank=True, null=True)
    ai = models.TextField(default='ai', blank=True, null=True)
    min_importante = models.CharField(max_length=8, blank=True, null=True)
    id_subpasta_pai = models.ForeignKey(SubPasta, on_delete=models.CASCADE, related_name='subpastas')

    def save(self, *args, **kwargs):
        # Verificar se já existe um BoardApp com o mesmo id_subpasta_pai
        existing_board_app = BoardApp.objects.filter(id_subpasta_pai=self.id_subpasta_pai).first()
        if existing_board_app:
            raise ValidationError('Já existe um BoardApp para esta subpasta.')

        super(BoardApp, self).save(*args, **kwargs)
  