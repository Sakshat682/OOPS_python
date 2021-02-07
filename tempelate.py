import webbrowser

class Movie():
    def __init__(self, name, poster, url):
        self.title = name
        self.poster_image_url = poster
        self.trailer_youtube_url = url

    # def show_trailer(self):
    #     webbrowser.open(url)
