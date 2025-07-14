#Lista de filmes
movies_list = ["titanic","the godfather", "inception", "jurassic park"]

# 1 - Iterando valores em uma lista
for movie in movies_list:
    print(movie)

# 2 - Quando a condição for atendida, o loop será encerrado
for movie in movies_list:
    if movie == "inception":
        break
    print(movie)

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração (Pulando a da condição)
for movie in movies_list:
    if movie == "inception":
        continue
    print(movie)

# 4 - Avaliação do filme
movie_name = input("Digite o nome do filme: \n")
movie_rating = int(input("Digite quantas avaliações deseja fazer: \n"))
total = 0 
for i in range(movie_rating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note

if movie_rating > 0:
    average = total/movie_rating
else:
    average = 0

print(f"A média de avaliação do {movie} é: {average:.2f}")