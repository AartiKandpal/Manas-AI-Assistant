import webbrowser
from urllib.parse import quote


class BrowserTools:

    @staticmethod
    def open_url(url: str):
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        webbrowser.open(url)
        return f"Opened {url}"

    @staticmethod
    def google_search(query: str):
        url = f"https://www.google.com/search?q={quote(query)}"
        webbrowser.open(url)
        return f"Searching Google for '{query}'"

    @staticmethod
    def youtube_search(query: str):
        url = f"https://www.youtube.com/results?search_query={quote(query)}"
        webbrowser.open(url)
        return f"Searching YouTube for '{query}'"

    @staticmethod
    def search_maps(location: str = None, query: str = None):
        """
        Accepts either:
        {"location": "Delhi"}
        or
        {"query": "Delhi"}
        """

        place = location or query

        if not place:
            return "No location provided."

        url = f"https://www.google.com/maps/search/{quote(place)}"
        webbrowser.open(url)
        return f"Searching Maps for '{place}'"

    @staticmethod
    def open_google():
        webbrowser.open("https://google.com")
        return "Opened Google"

    @staticmethod
    def open_youtube():
        webbrowser.open("https://youtube.com")
        return "Opened YouTube"

    @staticmethod
    def open_github():
        webbrowser.open("https://github.com")
        return "Opened GitHub"

    @staticmethod
    def open_chatgpt():
        webbrowser.open("https://chat.openai.com")
        return "Opened ChatGPT"

    @staticmethod
    def open_linkedin():
        webbrowser.open("https://linkedin.com")
        return "Opened LinkedIn"