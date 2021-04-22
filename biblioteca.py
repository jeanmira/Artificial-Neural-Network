# ------------------------------- /usr/bin/g++-7 ------------------------------#
# ------------------------------- coding: utf-8 -------------------------------#
# Criado por:   Jean Marcelo Mira Junior
# Versão: 1.0
# Criado em: 22/05/2021
# Sistema operacional: Linux - Ubuntu 20.04.1 LTS
# Python 3
# ------------------------------ Pacotes --------------------------------------#
import os
import csv
import numpy as np
import openpyxl

from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer
from pybrain3.structure.modules import SoftmaxLayer
from pybrain3.structure.modules import SigmoidLayer
# -----------------------------------------------------------------------------#


def analise(nomeDoArquivo):

    # Definição da rede
    # rede = buildNetwork(Neurônios camada de entrada, Neurônios camada oculta, Neurônios camada de  saída, Unidade de Bias(valor unitário conectado a um neurônio))
    rede = buildNetwork(1, 2, 1)
    base = SupervisedDataSet(1, 1)

    # Manipulação do arquivos
    diretorio = os.getcwd()  # Salva os nome caminho do diretorio

    arquivo = openpyxl.load_workbook(
        diretorio + "/" + nomeDoArquivo, data_only=True)
    folha = arquivo.active

    entrada = []
    saida = []

    for i in range(1, folha.max_row):
        entrada.append(int(folha.cell(row=i+1, column=2).value))
        saida.append(int(folha.cell(row=i+1, column=3).value))

    """ for i in range(len(entrada)):
        print(entrada[i], saida[i]) """

    # Alimentação na rede

    for i in range(len(entrada)):
        base.addSample((entrada[i]), (saida[i]))

    treinamento = BackpropTrainer(
        rede, dataset=base, learningrate=0.01, momentum=-0.06)

    for i in range(1, 5000):
        erro = treinamento.train()
        # if(i % 500 == 0):
        print("Erro:", erro)

    usuario = 0
    while(usuario != -1):
        usuario = input()
        print("Entrada: ")
        print("Saida: ", rede.activate(usuario))
