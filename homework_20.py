import requests
import json
import threading


class Images:

    def __init__(self, url, image_name):
        self.image_name = image_name
        self.url = url
        try:
            requests.get(self.url)
        except requests.exceptions.InvalidURL:
            raise requests.exceptions.InvalidURL("url is not valid")

    def download_image(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            with open(f"{self.image_name}.jpg", "wb") as image:
                image.write(response.content)
                print("Your image is downloaded")


with open("my_links.json", "r") as json_file:
    data = json.load(json_file)

for item in data:
    image = Images(item["img_url"], item["img_name"])
    my_image = threading.Thread(target=image.download_image())
    my_image.start()
    my_image.join()
