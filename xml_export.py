'''
Autor: Bruno Brito
Data: 23/03/2023

Objetivo: junção das classes read_export_xml.py e read_folder.py para criação
dos arquivos excel na pasta onde estão os arquivos xml originais
'''

# importando as classes
import read_folder as rf
import Read_export_xml_toExcel as rex

# inserir pastas com os arquivos xml
path = '/Users/brunobrito/Desktop/dev/xml'

# leitura dos arquivos na pasta
files = rf.Read_Files(path)
print(files.read_folder())
files_path = files.get_path()

# leitura de cada um dos arquivos xml e exportacao para excel
for i in files_path:
    xml = rex.Read_export_xml_toExcel(i, i, path)
    dict_xml = xml.read_xml()
    xml.export_excel(dict_xml)

