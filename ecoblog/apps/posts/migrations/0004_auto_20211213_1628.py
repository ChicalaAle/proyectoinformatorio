# Generated by Django 3.0 on 2021-12-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_categoria_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]