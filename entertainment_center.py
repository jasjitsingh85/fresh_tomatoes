import media
import fresh_tomatoes

# Instantiate movie object for Braveheart
braveheart_title = "Braveheart"
braveheart_image_url = "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg"
braveheart_youtube_url = "https://www.youtube.com/watch?v=wj0I8xVTV18"
braveheart = media.Movie(braveheart_title, braveheart_image_url, braveheart_youtube_url)

# Instantiate movie object for Moneyball
moneyball_title = "Moneyball"
moneyball_image_url = "http://www.sonypictures.com/movies/moneyball/assets/images/onesheet.jpg"
moneyball_youtube_url = "https://www.youtube.com/watch?v=-4QPVo0UIzc"
moneyball = media.Movie(moneyball_title, moneyball_image_url, moneyball_youtube_url)

# Instantiate movie object for Namesake
namesake_title = "Namesake"
namesake_image_url = "https://images-na.ssl-images-amazon.com/images/I/51-ByAXGEFL.jpg"
namesake_youtube_url = "https://www.youtube.com/watch?v=_sOaA-4Y8tI"
namesake = media.Movie(namesake_title, namesake_image_url, namesake_youtube_url)

# Add favorite movies to list
movies = [braveheart, moneyball, namesake]

# Open movies in web page
fresh_tomatoes.open_movies_page(movies)
