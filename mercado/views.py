from django.shortcuts import render
import requests as rqt


def stock_list(request):
    contex = {}
    return render(request, 'templates/base.html', context)


def home(request):
    pass

def getAll_cripto()

def get_stock():
    pass

def getAll_stock_list():
    get = rqt.get('https://www.dadosdemercado.com.br/acoes')
    pass