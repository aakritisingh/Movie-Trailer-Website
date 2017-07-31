import webbrowser

class Movie():
	#This class provides the details of the movie content stored in it

	#Next we are initializing and creating space in the memory for all the movie related cotents
    def __init__(self, movie_title, movie_desc, poster_image, youtube_trailor):
        self.movie_title = movie_title
        self.movie_desc = movie_desc
        self.poster_url = poster_image
        self.youtube_trailor_url = youtube_trailor

    def show_trailor(self):
        webbrowser.open(self.youtube_trailor_url)

    def show_poster(self):
        webbrowser.open(self.poster_url)

    
    
