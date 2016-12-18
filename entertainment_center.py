import media
import fresh_tomatoes

braveheart_title = "Braveheart"
braveheart_image_url = "XXX"
braveheart_youtube_url = "XXX"
braveheart = media.Movie(braveheart_title, braveheart_image_url, braveheart_youtube_url)

moneyball_title = "Moneyball"
moneyball_image_url = "XXX"
moneyball_youtube_url = "XXX"
moneyball = media.Movie(moneyball_title, moneyball_image_url, moneyball_youtube_url)

movies = [braveheart, moneyball]

fresh_tomatoes.open_movies_page(movies)
