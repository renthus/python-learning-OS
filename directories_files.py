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
