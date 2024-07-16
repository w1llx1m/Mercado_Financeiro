from django.shortcuts import render
import requests as rqt
from bs4 import BeautifulSoup
import json


def home(request):
    context = {'Context': getAll_stock_list()}
    return render(request, 'home.html', context)

def getAll_cripto():
    pass

def get_stock():
    pass

def getAll_stock_list():
    get = rqt.get('https://www.dadosdemercado.com.br/acoes')
    ret = get.content
    soup = BeautifulSoup(ret, 'html.parser').prettify()
    print(soup)
    
    return 'ola'