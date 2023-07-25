#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:41:35 2022

@author: cescobar

Basado en el libro:Python para Bioinformática, Sebastian Bassi
Este libro está a la venta en http://leanpub.com/pythonparabioinformatica
Esta versión se publicó en 2021-09-15

"""

"""
A un pH fijo es posible calcular la carga neta de una proteína sumando la carga de sus aminoácidos
individuales. Esto es una aproximación ya que no se tiene en cuenta si los aminoácidos están
expuestos u ocultos en la estructura de la proteína. Este programa tampoco tiene en cuenta el hecho
de que la cisteína agrega carga solo cuando no es parte de un puente disulfuro. Dado que es un valor
aproximado, los valores obtenidos deben considerarse como una estimación.
"""

prot_seq = input('Secuencia de la proteína: ')
charge = -0.002
prot_charge = {'C':-.045, 'D':-.999, 'E':-.998,
               'H':.091, 'K':1, 'R':1, 'Y':-.001}
for carga in prot_seq.upper():
    if carga in prot_charge:
        charge+= prot_charge[carga]
print(charge)
