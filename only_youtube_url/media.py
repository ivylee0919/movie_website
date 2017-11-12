import webbrowser

class Movie():
	"""
	The class Movie includes some information for a movie: 
	the title, the poster_image, the trailer and the duration.
	"""


	def __init__(self, movie_title, poster_image, trailer_url, movie_duration):
		"""
		Initialize the instance self with these attributes: 
		title, poster_image_url, trailer_youtube_url and duration.
		"""
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_url
		self.duration = movie_duration
