import xmltodict
import pandas as pd

#Abertura do arquivo xml e conversao para dicionario
xml_file = open('notas fiscais/35230308463170000114550010002623311021363913-procnfe.xml', 'r')
xml_string = xml_file.read()
python_dict = xmltodict.parse(xml_string)

#identificar o numero de itens em um xml
def count_items(xml_file):
    xml_string = xml_file.read()
    python_dict = xmltodict.parse(xml_string)
    return len(python_dict['nfeProc']['NFe']['infNFe']['det'])

print(count_items(xml_file))

a = {'item0':python_dict['nfeProc']['NFe']['infNFe']['det'][0]['prod']}
b = {'item1':python_dict['nfeProc']['NFe']['infNFe']['det'][1]['prod']}
c = {'item2':python_dict['nfeProc']['NFe']['infNFe']['det'][2]['prod']}
d = {'item3':python_dict['nfeProc']['NFe']['infNFe']['det'][3]['prod']}

#print(a)

#função para junção de dicionários
def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

lista_livros = merge_dicts(a, b, c,d)
lista_livros

#conversão de dicionários de dicionários em dataframe
df = pd.DataFrame(lista_livros).T



#funcao para criar dicionarios a partir de itens de uma xml
def create_dict(xml_file, item):
    xml_file = open(xml_file, 'r')
    xml_string = xml_file.read()
    python_dict = xmltodict.parse(xml_string)
    return python_dict['nfeProc']['NFe']['infNFe']['det'][item]['prod']