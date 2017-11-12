# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

her = media.Movie("Her",
				  "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
				  "https://www.youtube.com/watch?v=WzV6mXIOVl4")
prada = media.Movie("The Devil Wears Prada",
					"http://img3.mtime.com/mg/2008/8/f8100a07-7c8d-4e9a-b0f9-ff85345d2354.jpg",
					"https://www.youtube.com/watch?v=XTDSwAxlNhc")
pride_and_prejudice = media.Movie("Pride and Prejudice",
								  "http://www.xiexingcun.com/Photo/UploadPhotos/201201/2012012910543812.jpg",
								  "https://www.youtube.com/watch?v=7Afx8MGg00g")
zootopia = media.Movie("Zootopia",
					   "http://img31.mtime.cn/CMS/Gallery/2015/12/11/131226.99857115_1000.jpg", 
					   "http://v.youku.com/v_show/id_XMTI2MDU3MzgyOA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1#paction")
inside_out = media.Movie("Inside Out",
						 "http://ww1.sinaimg.cn/large/893c012ajw1epssf0h4ahj20kn0uk119.jpg",
						 "http://v.youku.com/v_show/id_XMTMzMTM3MTY2OA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
incredibles = media.Movie("The Incredibles",
						  "http://i-7.vcimg.com/trim/c9f9bbc13ac1d7895190dfcbc3b5ea9f888000/trim.jpg",
						  "http://v.youku.com/v_show/id_XMzE5MDUxNjM2.html?spm=a2h0j.8191423.module_basic_relation.5~5!2~5~5!4~5!2~1~3~A")

# make all the instances to be a list
movies = [her, prada, pride_and_prejudice, zootopia, inside_out, incredibles]

# make a html file to show all the movies
fresh_tomatoes.open_movies_page(movies)
