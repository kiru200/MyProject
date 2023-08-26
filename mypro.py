import requests
import json
from PIL import Image
from io import BytesIO
book_title = input("Enter the title of the book: ")
api_url = f"http://openlibrary.org/search.json?q={book_title}"
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    if "docs" in data and len(data["docs"]) > 0:
        first_result = data["docs"][0]
        title = first_result.get("title", "Title not found")
        author = first_result.get("author_name", ["Author not found"])
        first_publish_year = first_result.get("first_publish_year", "Year not found")
        book_subject=first_result.get("subject",["subjects not available"])
        book_language=first_result.get("language",["language not found"])
        print("\033[1m"+title+"\033[0m")
        print("\033[1m"+"Author:"+"\033[0m",",".join(author))
        print("\033[1m"+"First Edition:"+"\033[0m",first_publish_year)
        print("\033[1m"+"Subject:"+"\033[0m",",".join(book_subject))
        print("\033[1m"+"Language:"+"\033[0m",",".join(book_language))
        if "cover_i" in first_result:
            cover_id = first_result["cover_i"]
            cover_url = f"http://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
            if cover_url:
                response = requests.get(cover_url)
                if response.status_code == 200:
                   img = Image.open(BytesIO(response.content))
                   img.show()