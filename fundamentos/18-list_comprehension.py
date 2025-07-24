# 1 - Listando valores de 0 a 10 que sejam menores do que 4
list_numbers = [i for i in range(10) if i < 4]
print(list_numbers)

#Lista de filmes
movies_list = ["titanic","the godfather", "inception", "jurassic park"]

# 2 - Filmes que possuem a letra 'e' no título
movies_with_e = [movie for movie in movies_list if 'e' in movie.lower()]
print(movies_with_e)

# 3 - Filmes que eu assisti
movies_watched = [ movie for movie in movies_list if movie != "Jurassic Park"]
print(movies_watched)

# 4 - Encontrando um filme pelo nome
while True:
    search_name = input("Digite o nome do filme para buscar ou SAIR para encerrar: \n")
    if search_name.lower() == "sair":
        print("Programa encerrado!")
        break
    found_movies = [movie for movie in movies_list if search_name.lower() in movie.lower()]
    if found_movies:
        print(f"Filme(s) encontrado(s) com nome: {search_name}:")
        for found_movie in found_movies:
            print(found_movie)
        else:
            print(f"Nenhum filme foi encontrado com nome {search_name}. Tente novamente!")
