# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

urlBase = "http://jarroba.com/";
maxPages = 20;
counter = 0;

for i in range(1,maxPages):

    # Construyo la URL
    if i > 1:
        url = "%spage/%d/" %(urlBase,i);
    else:
        url = urlBase;

    # Realizamos la petición a la web
    req = requests.get(url);
    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code;
    if statusCode == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text);

        # Obtenemos todos los divs donde estan las entradas
        entradas = html.find_all('div',{'class':'col-md-4 col-xs-12'});

        # Recorremos todas las entradas para extraer el título, autor y fecha
        for entrada in entradas:
            counter += 1;
            titulo = entrada.find('span', {'class' : 'tituloPost'}).getText();
            autor = entrada.find('span', {'class' : 'autor'}).getText();
            fecha = entrada.find('span', {'class' : 'fecha'}).getText();

            # Imprimo el Título, Autor y Fecha de las entradas
            print "%d - %s  |  %s  |  %s" %(counter,titulo,autor,fecha);

    else:
        # Si ya no existe la página y me da un 400
        break;
