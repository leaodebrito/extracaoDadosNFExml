'''
Data: 22/03/2023
Autor: Bruno Brito

Objetivo: Leitura de arquivos xml e exportacao para excel
'''

endereco_arquivo = input('Digite o endereço do arquivo: ')
nome_excel = input('Digite o nome do arquivo excel: ')

#abertura de arquivo xml e conversao para dicionario
xml_file = open(endereco_arquivo, 'r')
xml_string = xml_file.read()
dict_xml = xmltodict.parse(xml_string)

#quantidade de itens no xml
def count_itens_xml(dicionario_xml):
    return len(dicionario_xml['nfeProc']['NFe']['infNFe']['det'])

#funcao para criar dicionarios a partir de itens de uma xml
def create_dict(dict_xml, item):
    return dict_xml['nfeProc']['NFe']['infNFe']['det'][item]['prod']

a = count_itens_xml(dict_xml)
print(a)

result = {}
for i in range(a):
    chave = 'item' + str(i)
    dicionario_do_item = create_dict(dict_xml, i)
    a = {chave:dicionario_do_item}
    result.update(a)


#criacao de Dataframe a partir do dicionario
df = pd.DataFrame(result).T

#exportacao de dataframe para excel
df.to_excel(nome_excel + '.xlsx')
