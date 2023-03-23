'''
Data: 23/03/2023
Autor: Bruno Brito

Objetivo: Leitura de arquivos de uma pasta e retorno dos endereços dos arquivos em uma lista
'''

import os

path = '/Users/brunobrito/Desktop/Dev/notas fiscais'

#ler arquivos de uma pasta
def read_folder(path):
    files = os.listdir(path)
    return files

#retornar endereco dos arquivos
def get_path(path):
    path_list = []
    files = os.listdir(path)
    for files in files:
        a = os.path.join(path, files)
        path_list.append(a)
    
    return path_list
   

print(get_path(path))