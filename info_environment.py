import os, platform

#verificando o nome do sistema operacional
nome_do_os = os.name
print("O nome do sistema operacional é: {}".format(nome_do_os))
print("#"*60)

#capturando o nome da plataforma
nome_da_plataforma = platform.system()
print("O nome da plataforma é: {}".format(nome_da_plataforma))
print("#"*60)

nome_ambiente = os.environ
print("O nome do ambiente operacional é: {}".format(nome_ambiente))
print("O HOMEPATH é: {}".format(nome_ambiente['HOMEPATH']))
print("O APPDATA é: {}".format(nome_ambiente['APPDATA']))
print("#"*60)

nome_processo_atual = os.getpid()
print("O id do processo que está sendo utilizado é o: {}".format(nome_processo_atual))
print("#"*60)

#captura o caminho atual
caminho_atual = os.getcwd()
print("O caminho deste arquivo é o: {}".format(caminho_atual))
print("#"*60)