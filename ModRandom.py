# Para começar, o python precisa importar o módulo para poder interpretar o seu uso:
import random

# o módulo random apresenta diversos usos, como choice, shuffle, randInt, o próprio random, uniform e outros
#por exemplo: Ao usar só Random:
print(random.random())
print("vai ser um número de entre 0 e 1\n\n")
#geralmente usado para porcentagem como em jogos

#já o randInt
print(random.randint(1, 20))
print("vai ser um número entre 1 e 20\n\n")
#como um randomizador mais simples pode ser usado para muitas coisas como jogar dados, sortear numeros

#você pode adicionar modificadores usando um randRange, que vai adicionar passos na sua execução
print(random.randrange(1, 20))
print(random.randrange(1, 20, 4))
print("usando um randrange sem passo, apenas será um número de 1 a 19 e com um passo de 4\n irá sortear de 1 a 20 que são múltiplos de 4\n\n")
#semelhante ao randint porem com especificação permitindo por exemplo buscar apenas valores impares

#é possível usar o random para estátisticas, como pontos flutuantes, desvios padrões etc
print(random.gauss(0, 1))     # Distribuição normal (média=0, desvio=1)
print(random.expovariate(1))  # Distribuição exponencial
print(random.uniform(5, 10))  # Vai gerar um ponto flutuante, perto de 7.alguma coisa
print("exemplo de estatisticas\n\n")

#usando listas ou vetores para exemplificar outros tipos, temos o choice ou shuffle
game = ["pedra", "papel", "tesoura"]
print(random.choice(game))#seleciona um valor podendo repetir de acordo com a quantidade exigida
print(game)
random.shuffle(game)#embaralha um grupo de dados dentro do proprio agrupamento, podendo ser utilizado por exemplo em um jogo de baralho
print(game)
print("o choice vai sortear algum elemnto da lista enquanto o shuffle pega essa lista e ordena ela aleatóriamente")
#em listas também é muito importante lembrar do sample, que pega essa lista e exibe seus elementos por n elementos
print(random.sample(game, 2))#ele vai retornar de forma aleatória 2 elementos da lista(sem repetições)


