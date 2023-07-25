#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:34:24 2022

@author: cescobar

Basado en el libro:Python para Bioinformática, Sebastian Bassi
Este libro está a la venta en http://leanpub.com/pythonparabioinformatica
Esta versión se publicó en 2021-09-15

"""

"""
El siguiente código calcula el peso molecular de una proteína basado en sus aminoácidos 
individuales. Dado que el aminoácido se almacena en una cadena, el programa recorrerá 
cada letra usando for.
"""

prot_seq = input('Ingrese la secuencia de la proteína: ')
prot_weight = {'A':89, 'V':117, 'L':131, 'I':131, 'P':115,
                'F':165, 'W':204, 'M':149, 'G':75, 'S':105,
                'C':121, 'T':119, 'Y':181, 'N':132, 'Q':146,
                'D':133, 'E':147, 'K':146, 'R':174, 'H':155}
total_weight = 0
for proteina in prot_seq:
    total_weight = total_weight + prot_weight.get(proteina.upper(), 0)
total_weight = total_weight - (18 * (len(prot_seq) - 1))
print('El peso neto es : {}'.format(total_weight))


i=0

while i < 10:
    print(i)
    i+=2