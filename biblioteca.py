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

    for i in range(1, interacoes):
        # print("[", i, "]")
        treinamento.train()

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
    for i in range(len(normalEntradaTeste)):
        dadoSaida.append(rede.activate([normalEntradaTeste[i]]))

    # Plot
    fig, axs = plt.subplots(2)
    # Visualizando os dados de erro e validação
    trnerr, valerr = treinamento.trainUntilConvergence(
        dataset=base, maxEpochs=10)
    axs[0].set_title('Dados de erro e validação')
    axs[0].plot(trnerr, 'b', valerr, 'r')

    axs[1].plot(normalSaidaTeste, color='green',
                label='Saída teste real')
    axs[1].plot(dadoSaida, color='red', label='Saída teste rede neural')
    axs[1].grid(True)
    # axs[1].legend()
    axs[1].set_title('Saída teste real x Saída teste rede neural')
    # plt.text(24, 0.06, "Número de interações: 50000")
    # plt.text(24, 0.01, "buildNetwork(1, 60, 60, 60, 60, 60, 1)")
    # plt.savefig("Dados_teste_5x60_50000.png")
    fig.tight_layout()
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
