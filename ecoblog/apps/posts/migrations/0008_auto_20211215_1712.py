# Generated by Django 3.0 on 2021-12-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_comentario_fechacreacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
