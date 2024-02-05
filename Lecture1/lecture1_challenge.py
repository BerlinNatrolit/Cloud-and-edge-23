# Copyright Robin Olsson, fråga han om ni vill ha något här. ;)

import os


import requests
from bs4 import BeautifulSoup

from urllib.parse import urlparse, urljoin



def fetch_latest_comic_url():
    # fetch + parse med BeautifulSoup
    response = requests.get('https://xkcd.com/')
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the latest comic image URL
    img_tag = soup.find('div', id='comic').find('img')
    img_url = urljoin('https://xkcd.com/', img_tag['src'])

    return img_url



def download_image(image_url, output_folder='.'):
    # Extract the img_name from url
    img_filename = urlparse(image_url).path.split('/')[-1]

    # Check if the image is already downloaded
    if os.path.exists(f'{output_folder}/{img_filename}'):
        print(F" Dagens Comic: {img_filename}: är redan där föefan.")
        return

    # Download the image
    img_response = requests.get(image_url)
    with open(f'{output_folder}/{img_filename}', 'wb') as img_file:
        img_file.write(img_response.content)

        print(F"Dagens Comic {img_filename}" " ner tankad!")

if __name__ == "__main__":
    latest_comic_url = fetch_latest_comic_url()
    download_image(latest_comic_url)