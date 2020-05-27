import fresh_tomatoes


import movie

toy_story = movie.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=wmiIUN-7qhE")

#print(toy_story.storyline)

avatar = movie.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)

#avatar.show_trailer()

fifty_shades_of_grey = movie.Movie("Fifty Shades of Grey", "A college graduate who begins a sadomasochistic relationship with young business magnate Christian Grey", "https://upload.wikimedia.org/wikipedia/en/7/73/Fifty_Shades_of_Grey_poster.jpg", "https://www.youtube.com/watch?v=SfZWFDs0LxA")

#fifty_shades_of_grey.show_trailer()
#fifty_shades_of_grey.show_trailer()


movies = [toy_story, avatar, fifty_shades_of_grey]

#fresh_tomatoes.open_movies_page(movies)

## upper case of VALID_RATINGS coz its constant

#print(movie.Movie.VALID_RATINGS)

print(movie.Movie.__doc__)
