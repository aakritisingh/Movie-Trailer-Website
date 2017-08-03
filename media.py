import webbrowser

class Movie():
	#This class provides the details of the movie content stored in it

	#Next we are initializing and creating space in the memory for all the movie related cotents
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailor):
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailor

    def show_trailor(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    
    
