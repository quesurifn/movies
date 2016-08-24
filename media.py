import webbrowser #imports webbrowser to call the function in show_trailer()

class Movie():
    """This class creates the variables to be called in entertainment_center.py
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        
    
    def show_trailer(self):
        """This function calls the input of the variable trailer_youtube and opens 
        it in the default web browser""" 
        webbrowser.open(self.trailer_youtube_url)
