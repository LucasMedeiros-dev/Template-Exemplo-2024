from django.urls import path
from . import views

urlpatterns = [

    # Padrão de URL para a página de detalhes do usuário
    path('', views.ReceberCEPView.as_view(), name='cep_form'),
    path('lista/', views.ListaCEPView.as_view(), name='cep_lista'),
    path('lista/<int:pk>/', views.DetalhesCEPView.as_view(), name='cep_detalhes'),

]
