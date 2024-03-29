# Generated by Django 5.0.3 on 2024-03-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViaCEP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viacep',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='viacep',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='viacep',
            name='localidade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='viacep',
            name='logradouro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='viacep',
            name='uf',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
