import requests
import json


class Images:

    def __init__(self, url, image_name):
        self.url = url
        self.image_name = image_name

    def is_valid_url(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return True
        else:
            print("usl is not valid")

    def download_image(self):
        response = requests.get(self.url)
        if self.is_valid_url():
            with open(f"{self.image_name}.jpg", "wb") as image:
                image.write(response.content)
                print("Your image is downloaded")


image_1 = Images(
    "https://img5.goodfon.com/wallpaper/nbig/9/10/mak-maki-tsvety-krasnye-makovoe-pole-iarkie-svet-oblaka-lug.jpg",
    "image1")
image_2 = Images(
    "https://img5.goodfon.com/wallpaper/nbig/9/10/2222222222222222222222222222222222222222222222222222222222.jpg",
    "image2")

image_1.download_image()
image_2.download_image()

with open("my_links.json", "r") as json_file:
    data = json.load(json_file)


for item in data:
    image = Images(item["img_url"], item["img_name"])
    image.download_image()



