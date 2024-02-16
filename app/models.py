from django.db import models
from uuid import uuid1

# Create your models here.

class App(models.Model):
       id_pasta = models.UUIDField(primary_key=True, default=uuid1, editable=False)
       nome = models.CharField(max_length=20)