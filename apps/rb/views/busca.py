from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from rb.models import Receita

def busca(request):
    
    busca_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        busca_receitas = busca_receitas.filter(nome_receita__icontains=nome_a_buscar)
    
    dados = {
        'receitas' : busca_receitas
    }
    
    return render(request, 'receitas/buscar.html', dados)
