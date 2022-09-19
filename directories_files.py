import os


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


#######################
#***CRIAR DIRETÓRIOS***
#######################

#Criando diretórios na pasta atual
pasta_I = 'primeiro_teste'
os.mkdir(pasta_I)
print("A pasta {} foi criado".format(pasta_I))
print("#"*60)

#criando diretórios em outras pastas
pasta = "Teste_Curso_Python_OS"
os.mkdir(r"C:\Users\renat\Desktop\{}".format(pasta))
print("#"*60)

#criando pasta dentro de outra pasta no mesmo diretório
pasta_II = "segundo_teste"
os.mkdir("primeiro_teste\\{}".format(pasta_II))
print("A pasta II {} foi criado".format(pasta_II))
print("#"*60)

#criando mais de uma pasta dentro da outra de uma só vez
#não é possível criar pastas de forma recursiva

#criando dois diretórios dentro do outro de uma só vez (para casos recursivos)
diretorio_1 = 'diretorio_1'
diretorio_2 = 'diretorio_2'
diretorio_3 = 'diretorio_3'
diretorio_4 = 'diretorio_4'
os.makedirs(diretorio_1+"\\"+diretorio_2+"\\"+diretorio_3+"\\"+diretorio_4)


######################################
#***MOVENDO E RENOMEANDO DIRETÓRIOS***
######################################

#renomeando um arquivo.txt
os.rename('arquivo1.txt', 'arquivo1_renomeado.txt')

#renomeando uma pasta
os.rename(diretorio_1,'diretorio_111')

#renomeando o arquivo e movendo ele para outra pasta
os.rename('arquivo1_renomeado.txt', "diretorio_111\\arquivo1_renomeado.txt")