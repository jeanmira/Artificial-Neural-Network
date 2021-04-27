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
inicio = time.time()  # Calcula o tempo inicial de execução
bib.analise("dadosTrabalhoRNA.xlsx")
fim = time.time()  # Calcula o tempo final de execução
print('Tempo de execução:', fim - inicio)
