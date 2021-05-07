# ------------------------------- /usr/bin/g++-7 ------------------------------#
# ------------------------------- coding: utf-8 -------------------------------#
# Criado por:   Jean Marcelo Mira Junior
#               Victor Philos Donato Luiz da Silva
# Versão: 1.0
# Criado em: 22/05/3021
# Sistema operacional: Linux - Ubuntu 30.04.1 LTS
# Python 3
# ------------------------------ Pacotes --------------------------------------#
import os
import openpyxl
import matplotlib.pyplot as plt
import pickle

from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer
# -----------------------------------------------------------------------------#


def analise(nomeDoArquivo):
    interacoes = 5000  # Número de interações
    fileObject = open('redesalva.xml', 'wb')  # Abre arquivo

    # Definição da rede
    # rede = buildNetwork(Neurônios camada de entrada, Neurônios camada oculta, Neurônios camada de  saída, Unidade de Bias(valor unitário conectado a um neurônio))
    base = SupervisedDataSet(1, 1)
    rede = buildNetwork(base.indim, 60, 60, 60, 60, 60, base.outdim)

    # Manipulação de arquivos
    diretorio = os.getcwd()  # Salva os nome caminho do diretório

    arquivo = openpyxl.load_workbook(
        diretorio + "/" + nomeDoArquivo, data_only=True)
    folha = arquivo.active

    entradaTreino = []
    saidaTreino = []
    entradaTeste = []
    saidaTeste = []

    for i in range(1, folha.max_row):
        if((i % 5) == 0):
            entradaTreino.append(float(folha.cell(row=i+1, column=2).value))
            saidaTreino.append(float(folha.cell(row=i+1, column=3).value))
        else:
            entradaTeste.append(float(folha.cell(row=i+1, column=2).value))
            saidaTeste.append(float(folha.cell(row=i+1, column=3).value))

    normalEntradaTreino = []
    normalSaidaTreino = []
    normalEntradaTeste = []
    normalSaidaTeste = []

    # Normaliza os dados
    for i in range(len(entradaTreino)):
        normalEntradaTreino.append(
            (entradaTreino[i]-min(entradaTreino))/(max(entradaTreino)-min(entradaTreino)))
        normalSaidaTreino.append(
            (saidaTreino[i]-min(saidaTreino))/(max(saidaTreino)-min(saidaTreino)))

    for i in range(len(saidaTeste)):
        normalEntradaTeste.append(
            (entradaTeste[i]-min(entradaTeste))/(max(entradaTeste)-min(entradaTeste)))
        normalSaidaTeste.append(
            (saidaTeste[i]-min(saidaTeste))/(max(saidaTeste)-min(saidaTeste)))

    """ for i in range(len(entrada)):
        print(entrada[i], saida[i]) """

    # Alimentação da rede neural artificial

    for i in range(len(normalEntradaTreino)):
        base.addSample(([normalEntradaTreino[i]]), ([normalSaidaTreino[i]]))

    treinamento = BackpropTrainer(rede, dataset=base, verbose=True)

    erro = 0
    for i in range(1, interacoes):
        # print("[", i, "]")
        erro += treinamento.train()
    erro /= interacoes

    pickle.dump(rede, fileObject)  # Guarda dados de treino
    fileObject.close()  # Fecha arquivo

    # Faz o gráfico dos dados de treino da saída real x saída da rede neural artificial (opcional)
    """ dadoSaida = []
    for i in range(len(entradaTreino)):
        dadoSaida.append(rede.activate([normalEntradaTreino[i]]))

    plt.figure(figsize=(7, 5))
    plt.plot(normalSaidaTreino, color='green',
             label='Saída treino real')
    plt.plot(dadoSaida, color='red', label='Saída treino rede neural')
    plt.grid(True)
    plt.legend()
    plt.title('Saída treino real x Saída treino rede neural')
    plt.text(24, 0.06, "Número de interações: 5000")
    plt.text(24, 0.01, "buildNetwork(1, 25, 25, 25, 25, 25, 1)")
    plt.savefig("Dados_treino_5x25_5000.png")
    plt.show() """

    # Avaliando a rede com os dados de teste, faz o gráfico dos dados de teste da saída real x saída da rede neural artificial
    dadoSaida = []
    for i in range(len(entradaTreino)):
        dadoSaida.append(rede.activate([normalEntradaTeste[i]]))

    plt.figure(figsize=(7, 5))
    plt.plot(normalSaidaTreino, color='green',
             label='Saída treino real')
    plt.plot(dadoSaida, color='red', label='Saída treino rede neural')
    plt.grid(True)
    plt.legend()
    plt.text(7, 0, "Erro: " + str(erro))
    plt.title('Saída teste real x Saída teste rede neural')
    plt.savefig("teste.png")
    plt.show()


def aplicacao():
    fileObject = open('redesalva.xml', 'rb')
    rede = pickle.load(fileObject)
    # Interação com o usuário
    """ usuario = 0
    while(usuario != -1):
        usuario = input()
        print("Entrada: ")
        n = rede.activate((usuario-min(entradaTreino)) /
                          (max(entradaTreino)-min(entradaTreino)))
        print("Saida: ", (n*max(entradaTreino)+min(entradaTreino)*(1-n))) """
