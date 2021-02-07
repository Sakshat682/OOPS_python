import tempelate
import page

movie1 = tempelate.Movie('My hero academia: Hero Rising',\
        'https://upload.wikimedia.org/wikipedia/en/1/1d/My_Hero_Academia_-_Two_Heroes_poster.jpg',\
        'https://www.youtube.com/watch?v=HAnSkhFlTHM')

movie2 = tempelate.Movie('Inception',\
        'https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg',\
        'https://www.youtube.com/watch?v=YoHD9XEInc0')

movie3 = tempelate.Movie('Demon Slayer: Infinity Train',\
        'https://www.boxofficepro.com/wp-content/uploads/2020/10/Demon-Slayer-the-Movie-Mugen-Train-cropped-poster.png',\
        'https://www.youtube.com/watch?v=ATJYac_dORw')

movie4 = tempelate.Movie('The Nun',\
        'https://upload.wikimedia.org/wikipedia/en/3/34/TheNunPoster.jpg',\
        'https://www.youtube.com/watch?v=pzD9zGcUNrw')

movie5 = tempelate.Movie('Kesari',\
        'https://upload.wikimedia.org/wikipedia/en/c/c4/Kesari_poster.jpg',\
        'https://www.youtube.com/watch?v=JFP24D15_XM')




# movie1.show_trailer()

movies = [movie1, movie2, movie3, movie4, movie5]
page.open_movies_page(movies)