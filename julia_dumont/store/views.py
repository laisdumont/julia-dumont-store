import os
from math import ceil
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator


def home(request):
    perpage = 5
    # Obter um parâmetro específico da query string
    page = int(request.GET.get('page', '1'))

    # Definir o caminho absoluto do diretório (ajustar conforme sua estrutura)
    path_directory = os.path.join(settings.BASE_DIR, 'store/static/images/clothes')

    # Listar todos os arquivos no diretório
    try:
        files = os.listdir(path_directory)
        # Filtrar somente arquivos (evitar diretórios)
        files = [f for f in files if os.path.isfile(os.path.join(path_directory, f))]

        start = perpage*page-perpage
        end = perpage*page

        photos = files[start:end]

        pages = [i for i in range(1, ceil(len(files) / perpage) + 1)]
        
        paginator = Paginator(files, 5)  # Exibe 3 fotos por página
        page_obj = paginator.get_page(page)
        return render(request, "../templates/home.html", {'request': request, 'files': photos, 'pages': pages, 'page': page, 'page_obj': page_obj})
    except FileNotFoundError:
        return HttpResponse('erro')

def clothes(request):
    perpage = 4
    # Obter um parâmetro específico da query string
    page = int(request.GET.get('page', '1'))

    # Definir o caminho absoluto do diretório (ajustar conforme sua estrutura)
    path_directory = os.path.join(settings.BASE_DIR, 'store/static/images/clothes')

    # Listar todos os arquivos no diretório
    try:
        files = os.listdir(path_directory)
        # Filtrar somente arquivos (evitar diretórios)
        files = [f for f in files if os.path.isfile(os.path.join(path_directory, f))]

        start = perpage*page-perpage
        end = perpage*page

        photos = files[start:end]

        pages = [i for i in range(1, ceil(len(files) / perpage) + 1)]
        
        paginator = Paginator(files, 4)  # Exibe 3 fotos por página
        page_obj = paginator.get_page(page) 

        return render(request, "../templates/clothes.html", {'request': request, 'files': photos, 'pages': pages, 'page': page, 'page_obj': page_obj})
    except FileNotFoundError:
        return HttpResponse('erro')

def singUp(request):
    return render(request, "../templates/singUp.html", {'request': request})