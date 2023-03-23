'''
Data: 23/03/2023
Autor: Bruno Brito

Objetivo: Leitura de arquivos de uma pasta e retorno dos endereços dos arquivos em uma lista
'''

import os

path = '/Users/brunobrito/Desktop/Dev/notas fiscais'

#class para leitura de arquivos
class ReadFiles:
    def __init__(self, path):
        self.path = path
    
    #leitura dos arquivos na pasta
    def read_folder(self):
        files = os.listdir(self.path)
        return files

    #retorna os endereços dos arquivos em formato de lista
    def get_path(self):
        path_list = []
        files = os.listdir(self.path)
        for files in files:
            if files[-4:] == '.xml':
                a = os.path.join(self.path, files)
                path_list.append(a)
        
        return path_list
    
a = ReadFiles(path)
print(a.get_path())