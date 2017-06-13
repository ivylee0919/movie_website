# Mini-Project: Movies Website

import media
import fresh_tomatoes

# define instances of the class Movie defined in media.py
her = media.Movie("Her",
				  "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",  # noqa
				  "https://www.youtube.com/watch?v=WzV6mXIOVl4",
				  "2h 6min")
prada = media.Movie("The Devil Wears Prada",
					"http://img3.mtime.com/mg/2008/8/f8100a07-7c8d-4e9a-b0f9-ff85345d2354.jpg",  # noqa
					"https://www.youtube.com/watch?v=XTDSwAxlNhc",
					"1h 49min")
pride_and_prejudice = media.Movie("Pride and Prejudice",
								  "http://www.xiexingcun.com/Photo/UploadPhotos/201201/2012012910543812.jpg",  # noqa
								  "https://www.youtube.com/watch?v=7Afx8MGg00g",
								  "2h 9min")
zootopia = media.Movie("Zootopia",
					   "http://img31.mtime.cn/CMS/Gallery/2015/12/11/131226.99857115_1000.jpg",  # noqa
					   "https://www.youtube.com/watch?v=jWM0ct-OLsM",
					   "1h 48min")
inside_out = media.Movie("Inside Out",
						 "http://ww1.sinaimg.cn/large/893c012ajw1epssf0h4ahj20kn0uk119.jpg",  # noqa
						 "https://www.youtube.com/watch?v=seMwpP0yeu4",
						 "1h 35min")
incredibles = media.Movie("The Incredibles",
						  "http://i-7.vcimg.com/trim/c9f9bbc13ac1d7895190dfcbc3b5ea9f888000/trim.jpg",  # noqa
						  "https://www.youtube.com/watch?v=eZbzbC9285I",
						  "1h 55min")

# make all the instances to be a list
movies = [her, prada, pride_and_prejudice, zootopia, inside_out, incredibles]

# make a html file to show all the movies
fresh_tomatoes.open_movies_page(movies)
