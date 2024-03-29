# Generated by Django 5.0.2 on 2024-02-27 14:59

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_subpasta_id_subpasta_boardapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardapp',
            name='id_board_app',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='boardapp',
            name='min_importante',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='subpasta',
            name='id_subpasta',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]
