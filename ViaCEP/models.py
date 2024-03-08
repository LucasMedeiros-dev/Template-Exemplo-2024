from django.db import models

# Create your models here.

# Define o modelo para o CEP
class ViaCEP(models.Model):
    cep = models.CharField(max_length=8) # CEP
    logradouro = models.CharField(max_length=100, null=True, blank=True) # Logradouro = Rua
    complemento = models.CharField(max_length=100, null=True, blank=True) # Complemento
    bairro = models.CharField(max_length=100, null=True, blank=True) # Bairro
    localidade = models.CharField(max_length=100, null=True, blank=True) # Localidade = Cidade
    uf = models.CharField(max_length=2, null=True, blank=True) # UF = Unidade Federativa
    
    # Tem vários campos que desejamos receber e salvar do ViaCEP.

    def __str__(self):
        return self.cep