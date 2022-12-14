import os, platform, shutil

#verificando o nome do sistema operacional
nome_do_os = os.name
print("O nome do sistema operacional é: {}".format(nome_do_os))
print("#"*60)
###############################################################

#capturando o nome da plataforma
nome_da_plataforma = platform.system()
print("O nome da plataforma é: {}".format(nome_da_plataforma))
print("#"*60)
##############################################################

nome_ambiente = os.environ
print("O nome do ambiente operacional é: {}".format(nome_ambiente))
print("O HOMEPATH é: {}".format(nome_ambiente['HOMEPATH']))
print("O APPDATA é: {}".format(nome_ambiente['APPDATA']))
print("#"*60)
###################################################################

nome_processo_atual = os.getpid()
print("O id do processo que está sendo utilizado é o: {}".format(nome_processo_atual))
print("#"*60)
######################################################################################

#captura o caminho atual através do diretório
caminho_atual = os.getcwd()
print("O caminho deste arquivo é o: {}".format(caminho_atual))
print("#"*60)
##############################################################

#captura o arquivo atual
print("O nome do diretório do arquivo atual é: ",__file__)
print("#"*60)
##########################################################

#nome do arquivo
print("Nome do arquivo atual: ",os.path.basename(__file__))
print("#"*60)
###########################################################

#pasta do arquivo
print("O nome da pasta do arquivo é: ", os.path.dirname(__file__))
print("#"*60)
##################################################################

#capturar a pasta + nome do arquivo (caminho absoluto)
print("O caminho absoluto do arquivo é: ", os.path.abspath(__file__))
print("#"*60)
#####################################################################


##########################
#***LISTANDO DIRETÓRIOS***
##########################

#listar todo o conteúdo de uma pasta
#deixando vazio irá mostrar todos os arquivos
conteudo_pasta = os.listdir()
print("Esta pasta contém os arquivos: {}".format(conteudo_pasta))
print("#"*60)

#lista todos os diretório e arquivos a partir do C:\\
conteudo_c = os.listdir("C:\\")
print("O diretório C:\\ contém: {}".format(conteudo_c))
print("#"*60)

#lista todos os diretórios e arquivos através de um caminho relativo
conteudo_caminho_relativo = os.listdir('venv\\')
print("O caminho relativo é: {}".format(conteudo_caminho_relativo))
print("#"*60)

##########################
##########################


#######################
#***CRIAR DIRETÓRIOS***
#######################

#Criando diretórios na pasta atual
pasta_I = 'primeiro_teste'
os.mkdir(pasta_I)
print("A pasta {} foi criado".format(pasta_I))
print("#"*60)
##############################################

#criando diretórios em outras pastas
pasta = "Teste_Curso_Python_OS"
os.mkdir(r"C:\Users\renat\Desktop\{}".format(pasta))
print("#"*60)
####################################################

#criando pasta dentro de outra pasta no mesmo diretório
pasta_II = "segundo_teste"
os.mkdir("primeiro_teste\\{}".format(pasta_II))
print("A pasta II {} foi criado".format(pasta_II))
print("#"*60)
#######################################################

#criando mais de uma pasta dentro da outra de uma só vez
#não é possível criar pastas de forma recursiva

#criando dois diretórios dentro do outro de uma só vez (para casos recursivos)
diretorio_1 = 'diretorio_1'
diretorio_2 = 'diretorio_2'
diretorio_3 = 'diretorio_3'
diretorio_4 = 'diretorio_4'
os.makedirs(diretorio_1+"\\"+diretorio_2+"\\"+diretorio_3+"\\"+diretorio_4)
##############################################################################

#######################
#######################


######################################
#***MOVENDO E RENOMEANDO DIRETÓRIOS***
######################################

#renomeando um arquivo.txt
os.rename('arquivo1.txt', 'arquivo1_renomeado.txt')
###################################################

#renomeando uma pasta
os.rename(diretorio_1,'diretorio_111')
######################################

#renomeando o arquivo e movendo ele para outra pasta
os.rename('arquivo1_renomeado.txt', "diretorio_111\\arquivo1_renomeado.txt")
############################################################################

######################################
######################################


########################
#***COPIANDO ARQUIVOS***
########################

import os
import shutil

#copia um arquivo em sua origem para a pasta de destino
pasta_arquivo_origem = os.getcwd() + "\\arquivo1.txt"
pasta_destino = os.getcwd() + "\\diretorio_1"
shutil.copy2(pasta_arquivo_origem,pasta_destino)
#######################################################

#copia um arquivo em sua origem para a pasta de destino e renomeando o arquivo
pasta_arquivo_origem = os.getcwd() + "\\arquivo_1.txt"
pasta_destino = os.getcwd() + "\\diretorio_1"
nome_arquivo_destino = "\\arquivo1_renomeado.txt"
shutil.copy2(pasta_arquivo_origem,pasta_destino + nome_arquivo_destino)
##############################################################################

########################
########################


#################################
#***COPIANDO ARQUIVOS E PASTAS***
#################################

from distutils.dir_util import copy_tree

#copia todo o conteúdo de uma pasta de origem para a pasta de destino
pasta_origem = os.getcwd() + "\\diretorio_1"
pasta_destino = os.getcwd() + "\\primeiro_teste"
copy_tree(pasta_origem, pasta_destino)
#####################################################################

#################################
#################################


##################################
#***REMOVENDO ARQUIVOS E PASTAS***
##################################

#removendo um arquivo (NÃO REMOVE PASTAS)
os.remove("primeiro_teste\\arquivo1_renomeado.txt")
###################################################

#remove pastas (NÃO REMOVE PASTAS CASO NÃO ESTEJAM VAZIAS
os.removedirs("primeiro_teste\\diretorio_2\\diretorio_3\\diretorio_4")
os.removedirs("diretorio_1\\diretorio_2\\diretorio_3\\diretorio_4")
######################################################################

#remove a pasta e todo o seu conteúdo passando por parâmetro
#a localização da pasta
shutil.rmtree("primeiro_teste")
shutil.rmtree("diretorio_1")
############################################################

##################################
##################################


#################################################
#***CHECANDO A EXISTÊNCIA DE ARQUIVOS E PASTAS***
#################################################

import os.path

#verifica se uma pasta existe e caso não exista, cria uma
if not os.path.isdir('desafio'):
    os.mkdir("desafio")
if not os.path.isdir('desafio\\teste'):
    os.mkdir('desafio\\teste')
#########################################################

#verifica se um arquivo existe numa determinada pasta
if not os.path.isfile('desafio\\arquivo.txt'):
    print("Arquivo não existe")
else:
    print("Arquivo existe")
#####################################################

#verifica se um arquivo ou pasta existem
#pasta
if not os.path.exists('desafio'):
    os.mkdir("desafio")
if not os.path.exists('desafio\\teste'):
    os.mkdir('desafio\\teste')
#arquivo
if not os.path.exists('desafio\\arquivo.txt'):
    print("Arquivo não existe")
else:
    print("Arquivo existe")
########################################

#################################################
#################################################


#######################
#***CRIANDO ARQUIVOS***
#######################

# open('desafio\\nome.txt', 'a') #appende => adiciona o conteúdo e não deleta
os.mkdir('desafio')
open('desafio\\nome.txt', 'w+') #write => deleta o conteúdo e escreve novamente
###############################################################################

#######################
#######################


###################################################
#***DESAFIO - PASTAS E ARQUIVOS***
#criar 10 pastas onde cada pasta possui 10 arquivos
###################################################

import os

diretorio = 'desafio'

#verificando se a pasta principal - diretório existe
if not os.path.exists(diretorio):
    os.mkdir(diretorio)
####################################################

#criando as pastas e os arquivos dentro das pastas
for i in range(1,11):
    if not os.path.exists(diretorio + "\\pasta_" + str(i)):
        os.mkdir(diretorio + "\\pasta_" + str(i))
    for j in range(1,11):
        open(diretorio + "\\pasta_" + str(i) + "\\arquivo_" + str(j) + ".txt", "w+")
    ####################################################################################

###################################################
###################################################