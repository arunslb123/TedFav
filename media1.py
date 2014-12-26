import webbrowser
class Ted():
    def __init__(self,ted_title,poster_image,trailer_youtube):
        self.title=ted_title
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
