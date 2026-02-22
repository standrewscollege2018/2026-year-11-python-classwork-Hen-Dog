'''movie thingy'''

movies = []
print("Enter your 3 favourite tv movies / shows from most favourite to least favourite")
for i in range(3):
    input("Enter name of movie:")

    movies.append(input("Enter name of movie:"))
    print(movies)

for i in range(len(movies)):
    print(f"{i}. {movies[i]}")