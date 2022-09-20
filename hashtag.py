from pathlib import Path

############################################
#***Listar todos os arquivos de uma pasta***
############################################

#local da pasta onde estamos trabalhando
print(Path.cwd())
########################################

#local da pasta num diretório qualquer
caminho = Path('C:/workspace/ProjetosPython/python-learning-OS/Arquivos_Lojas/') #usando o caminho completo o python irá imprimir o caminho completo
caminho = Path('Arquivos_Lojas/') #usando o caminho relativo o python imprime o caminho relativo
print(caminho)
######################################

#listar todos os arquivos dentro de uma pasta
arquivos = caminho.iterdir()
for arquivo in arquivos:
    print(arquivo)
print('#'*60)
    #########################################

############################################
############################################


#######################################################
#***Verificando se um arquivo existe dentro da pasta***
#######################################################

if Path('Arquivos_Lojas/202003_Bourbon_SP.csv').exists(): #caminho absoluto
    print('Arquivo existe')

if (caminho / Path('202003_Bourbon_SP.csv')).exists(): #caminho relativo
    print('Arquivo existe')

#######################################################
#######################################################


################################
#***Como criar uma pasta nova***
################################

#criando uma pasta
Path('Pasta Auxiliar').mkdir()
##############################

#criando uma pasta dentro de outra
Path('Pasta Auxiliar/Pasta2').mkdir()
#####################################

#copiando um arquivo para outra pasta
import shutil

arquivo_origem = Path('Arquivos_Lojas/202004_JK Iguatemi_SP.csv')
pasta_destino = Path('Pasta Auxiliar/202004_JK Iguatemi_SP_v2.csv')
shutil.copy2(arquivo_origem,pasta_destino)
print('Arquivo copiado')
print('#'*60)
###################################################################

#movendo um arquivo de uma pasta para outra pasta
import shutil

arquivo_origem = Path('Pasta Auxiliar/202004_JK Iguatemi_SP_v2.csv')
pasta_destino = Path('Pasta Auxiliar/Pasta2/202004_JK Iguatemi_SP_v3.csv')
shutil.move(arquivo_origem,pasta_destino)
print('Arquivo movido')
print('#'*60)
###################################################################

################################
################################


##############
#***DESAFIO***
##############

from pathlib import Path
import shutil

estados = ['RJ','SP','MG','GO','AM']

for estado in estados:
    Path('Arquivos_Lojas/' + estado).mkdir()

caminho = Path('Arquivos_Lojas/')
arquivos = caminho.iterdir()
for arquivo in arquivos:
    nome_arquivo = arquivo.name
    if nome_arquivo[-3:] == 'csv':
        estado = nome_arquivo[-6:-4]
        local_destino = caminho / Path(estado,nome_arquivo)
        shutil.move(arquivo,local_destino)
###########################################################