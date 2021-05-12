# ------------------------------- /usr/bin/g++-7 ------------------------------#
# ------------------------------- coding: utf-8 -------------------------------#
# Criado por:   Jean Marcelo Mira Junior
#               Victor Philos Donato Luiz da Silva
# Versão: 1.0
# Criado em: 22/05/2021
# Sistema operacional: Linux - Ubuntu 20.04.1 LTS
# Python 3
# ------------------------------ Pacotes --------------------------------------#
import biblioteca as bib
import time
# -----------------------------------------------------------------------------#

usuario = input("Deseja treinar a rede < 1 para sim / 2 para não >: ")

if(usuario == "1"):
    inicio = time.time()  # Calcula o tempo inicial de execução
    bib.analise("dadosTrabalhoRNA.xlsx")
    fim = time.time()  # Calcula o tempo final de execução
    print('Tempo de execução:', fim - inicio)

if(usuario == "2"):
    min, max = bib.retornaMinMax("dadosTrabalhoRNA.xlsx")
    bib.aplicacao(min, max)