'''
Data: 23/03/2023
Autor: Bruno Brito

Objetivo: junção das classes read_export_xml.py e read_folder.py para criação
dos arquivos excel na pasta onde estão os arquivos xml originais
'''

import read_folder as rf
import read_export_xml as rex

#inserir pastas com os arquivos xml
path = '/Users/brunobrito/Desktop/Dev/notas fiscais'

#leitura dos arquivos na pasta
files = rf.Read_Files(path)
files_path = files.get_path()

#leitura de cada um dos arquivos xml e exportacao para excel
for i in files_path:
    xml = rex.Read_export_xml_toExcel(i, i[-17:-4], path)
    dict_xml = xml.read_xml()
    xml.export_excel(dict_xml)

