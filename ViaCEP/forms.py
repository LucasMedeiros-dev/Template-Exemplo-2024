from django import forms

# Define o Formulário para Receber o CEP no Django
class CepForm(forms.Form):
    cep = forms.CharField(label='CEP', max_length=8, required=True) # Define o campo CEP
    # O campo cep é do tipo CharField, que é um campo de texto. Tem tamanho máximo de 8 caracteres e é obrigatório.