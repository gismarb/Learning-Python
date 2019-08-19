# Quando usamod FROM "arquivo" IMPORT "Classe", estamos 
# fazendo uso das classes que criamos
from dado import Dado
from jogador import Jogador
from jogo import Jogo

# A classe "os" tem ferramentas de manipulacao de sistemas, como system("") no C e C++
import os

# Limpa tela
os.system('clear') or None

# Criando uma string para o titulo
titulo = 'Jogo de Dados'

# Tamanho da largura da linha
base = int(120)

# Criando uma string para a borda (imprimira 120 vezes *)
borda = '*' * base

# Imprimindo mensagem do Titulo
print(borda)
print(titulo.center(base))
print(borda)

# Imprimindo Regras
print("\nRegras:")
print("\t1) Cada Jogador pode jogar DOIS DADOS por vez;")
print("\t2) O primeiro jogador que SOMAR 7 com a sequencia da FACE dos 2 DADOS, vence, e o jogo e finalizado;")
print("\t3) Caso nenhum JOGADOR SOME 7, com suas jogadas, o jogo e finializado.\n")

# Iniciando Jogadas
jogadas = int(0)

# Rotina do Jogo
while (jogadas != 3 or Jogo.getResultado() != 7):
    Jogador.__init__(Ricardo')