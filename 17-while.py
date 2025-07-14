#Lista de filmes
movies_list = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valoresd e uma lista de filmes usando while
index = 0

#Enquanto meu índice for menor que o comprimento da minha lista...
while index < len(movies_list):
    #Imprimo o índice que estou
    print(movies_list[index])
    #Incremento em um o meu índice
    index += 1

# 2 - Quando a condição for atendida, o loop será encerrado
index = 0
while index < len(movies_list):
    if movies_list[index] == "Inception":
        break
    print(movies_list[index])
    index += 1

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
index = 0
while index < len(movies_list):
    if movies_list[index] == "Inception":
        index +=1
        continue
    print(movies_list[index])
    index += 1

# 4 - Avaliação do filme com o while
index = 0
movie_name = input("Digite o nome do filme: \n")
movie_rating = int(input("Digite quantas avaliações deseja fazer: \n"))
total = 0
count = 0

while count < movie_rating:
    note = float(input("Digite a nota para o filme: \n"))
    total += note
    count += 1

if movie_rating > 0:
    average = total / movie_rating
else:
    average = 0

print(f"A média de avaliação do filme {movie_name} é: {average:.2f}")