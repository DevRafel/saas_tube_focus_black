# Generated by Django 5.0.2 on 2024-02-21 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_subpasta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subpasta',
            name='pasta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subpastas', to='app.pasta'),
        ),
    ]