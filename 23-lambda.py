# Função potência de um número
power = lambda num: num ** 2
print(power(5))
print(power(9))

# Função que verifica se um número é par
is_even = lambda x:x % 2 == 0

print(is_even(27))
print(is_even(30))

# Função que divide um número por outro
div_num = lambda x,y: x/y

print(div_num(10,2))
print(div_num(32,4))

# Função que inverte uma string
reverse_string = lambda s:s[::-1]

print(reverse_string("Python"))
print(reverse_string("Javascript"))

#Funcionalidade relacionadas aos filmes:
movies_list = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "The Matrix"]
rating = {
    "Titanic": [8.5, 9.0, 7.5],
    "The Godfather": [9.5, 8.0, 9.8],
    "Inception": [8.0, 8.5, 7.0],
    "Jurassic Park": [7.5, 8.5, 7.0],
    "The Matrix": [8.8, 9.2, 8.5]
}
#Função para calcular a média de avaliações de um filme
average_rating = lambda movie_name: sum(rating[movie_name]) / len(rating[movie_name])

print(f"Média de avaliação do filme The Matrix: {average_rating("The Matrix"):.2f}")

#Função que verifica se um filmes está na lista
check_movie = lambda movie_name: movie_name in movies_list

print(f"Inception está na lista? {check_movie("Inception")}")

#Função para recomendar um filme com base na avaliação média
recomend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com media {average_rating(movie_name):.2f}"

print(f"{recomend_movie("Titanic")}")