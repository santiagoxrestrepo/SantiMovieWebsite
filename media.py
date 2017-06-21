import webbrowser

class Movie(object):

    """This class was created to hold the movie information which includes
        -Title
        -Story Line
        -Poster Image
        -Youtube Trailer
    """


# This creates the different variables

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# This playes the movie trailer in the browser        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
      
