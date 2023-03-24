'''
Data: 23/03/2023
Autor: Bruno Brito

Objetivo: Leitura de arquivos xml e exportacao para excel
'''

import pandas as pd
import xmltodict

class Read_export_xml_toExcel:
    def __init__(self, path, excel_name, exit_folder):
        self.path = path
        self.excel_name = excel_name
        self.exit_folder = exit_folder
        
    #abertura de arquivo xml e conversao para dicionario
    def read_xml(self):
        xml_file = open(self.path, 'r')
        xml_string = xml_file.read()
        dict_xml = xmltodict.parse(xml_string)
        return dict_xml
    
    #quantidade de itens no xml
    def count_itens_xml(self, dict_xml):
        return len(dict_xml['nfeProc']['NFe']['infNFe']['det'])
    
    #funcao para criar dicionarios a partir de itens de uma xml
    def create_dict(self, dict_xml, item):
        return dict_xml['nfeProc']['NFe']['infNFe']['det'][item]['prod']
    
    def export_excel(self, dict_xml):
        result = {}
        for i in range(self.count_itens_xml(dict_xml)):
            chave = 'item' + str(i)
            dicionario_do_item = self.create_dict(dict_xml, i)
            a = {chave:dicionario_do_item}
            result.update(a)
        
        #exportacao para excel na pasta de leitura do xml
        df = pd.DataFrame(result).T
        df.to_excel(self.excel_name[:-4] + '.xlsx')

