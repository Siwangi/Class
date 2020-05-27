## Class


import webbrowser



class Movie:
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, title, storyline, poster_image_url, trailer_url ):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
        webbrowser.open(self.poster_image_url)




## Constructor --initialize (__init__)

## Self -- reference of the object -- toy_story, avatar

## Instances(Object) -- toy_story, avatar

##  Instance-Variables -- title, storyline, poster_image_url, trailer_url



toy_story = Movie("Toy Story", "A story of a boy and his toys that come to life", "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=wmiIUN-7qhE")

avatar = Movie("Avatar", "A marine on an alien planet", "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")


##function inside class is instance method/function

print(toy_story.title)

print(avatar.title)

