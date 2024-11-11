
#Allows users to maintain a database of movies watched
movie_info = {}

#work on showing a user menu to link to the functions at will

#function to add a movie
def add_movie():
    new_movie = {}
    title = input("what is the movie title? ")
    new_movie['name'] = title
    new_movie_id = len(movie_info)
    movie_info[new_movie_id] = new_movie
    year = input("What year was this film released? ")
    new_movie['year'] = int(year)
    director = input("Who directed this film? ")
    new_movie['director'] = director
    rating = input("How would you rate this movie? 1-5 ")
    new_movie['rating'] = int(rating)

        

#function to prompt user if they want to print their library
def view_movies():
    ask_view = input("Would you like to view your library? Y/N ")
    if ask_view == 'y':
        for movie in movie_info:
            print(movie_info[movie])

#function to delete a dictionary entry via movie_id
def delete_movie():
    user_input = int(input('Input the ID Number of the movie to be deleted: '))
    if user_input in movie_info:
        del movie_info[user_input]

print("Let's build a database of every movie you have ever seen with your personal rating of each film!")
add = True    
while add:
    start = input("Would you like to add a movie? Y/N ")
    if start.lower() == 'y':
        add_movie()
    else:
        break

view_movies()

deletion = True
while deletion == True:
    ask_to_delete = input("Would you like to delete a movie? Y/N ")
    if ask_to_delete.lower() == 'y':
        print(movie_info)
        delete_movie()
    else:
        break

    
ask_finish = input("Would you like to view your current watch list one more time? Y/N ")
if ask_finish.lower() == 'y':
    for movie in movie_info:
            print(movie_info[movie])
else:
    print("Goodbye, fellow Cinephile!")


    








