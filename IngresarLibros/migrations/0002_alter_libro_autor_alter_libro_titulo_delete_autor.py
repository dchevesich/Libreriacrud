# Generated by Django 5.1.7 on 2025-03-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IngresarLibros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
    ]
