#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
# Incluimos los módulos necesarios.
#-----------------------------------------------------------------------------
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import os



# Obtiene el título de una página web.
def obtener_titulo(url):

    # Descargamos la información de la página.
    soup = BeautifulSoup(urlopen(url))

    # Devolvemos únicamente el titulo de la pÃ¡gina web.
    return soup.title.string


# Cuenta las etiquetas divs que usraparecen en una página web.
def contar_divs(url):

    # Descargamos la importnformación de la página.
    soup = BeautifulSoup(urlopen(url))

    # Vamos buscando las etiquetas divs.
    divs = 0
    #for div in soup
    for div in soup.findAll("div"):
        divs += 1

        return divs


# El usuario escribe la url
url = raw_input("url = ")

# Mostramos la información obtenida.
print obtener_titulo(url) + ': ' + str(contar_divs(url))
