
from django.views.generic import DetailView, CreateView, ListView # Importa as classes TemplateView, CreateView e ListView
from .forms import CepForm # Importa o formulário CepForm
from .models import ViaCEP # Importa o modelo ViaCEP
import requests # Importa a biblioteca requests para fazer requisições HTTP
from django.http import HttpResponseRedirect # Importa a classe HttpResponseRedirect para redirecionar o usuário

# Create your views here.
class ReceberCEPView(CreateView):
    template_name = 'inserir_cep.html'
    success_url = '/lista'
    model = ViaCEP
    fields = ['cep']

    def form_valid(self, form):
        # Recebe o cep do formulário para ser usado na requisição
        cep = form.cleaned_data.get('cep','00000000')
       
        url = f'https://viacep.com.br/ws/{cep}/json/'
        resposta = requests.get(url)

        dados = resposta.json()

        dados_meu_cep = {
            'logradouro': dados.get('logradouro',''),
            'complemento': dados.get('complemento',''),
            'bairro': dados.get('bairro',''),
            'localidade': dados.get('localidade',''),
            'uf': dados.get('uf','')
        }

        cep = ViaCEP.objects.update_or_create(cep=cep, defaults=dados_meu_cep)
        

        return HttpResponseRedirect(self.success_url)

class ListaCEPView(ListView):
    model = ViaCEP
    template_name = 'exibir_ceps.html'
    context_object_name = 'ceps'
    def get_queryset(self):
        return ViaCEP.objects.all()
    
class DetalhesCEPView(DetailView):
    model = ViaCEP  # Define o modelo a ser utilizado
    template_name = 'detalhe_cep.html'  # Define o nome do template a ser renderizado
    context_object_name = 'cep'  # Define o nome da variável de contexto para o objeto CEP

