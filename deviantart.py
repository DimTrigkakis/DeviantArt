import urllib
import os
import random

def fetch_url(url, path):
    urllib.urlretrieve(url, path)

def random_html_image(html):
    # find a random image in the html and return its http address in quotes
    d = html.split(" ")
    urls = []
    for i in d:
        if 'fixed_height' not in i:
            continue
        if 'src=' not in i:
            continue
        i = i[5:-1]
        urls.append(i)

    return random.choice(urls)

def extract_urls(html,folder):
    folder =  "C:\\Users\\Dimitris\\Desktop\\DeviantArt\\"+folder

    url = random_html_image(html)
    name = url.split('/')[-1]

    if not os.path.isdir(folder):
        print folder
        os.mkdir(folder)

    fetch_url(url, folder+"/"+name)

def generate_questions():

    terms = []
    with open("C:\\Users\\Dimitris\\Desktop\\DeviantArt\\Terms.txt") as f:
        for line in f:
            terms.append(line)
    return random.choice(terms)

def main_routine():
    foundation = "http://www.deviantart.com/browse/all/?q="
    question = generate_questions()

    response = urllib.urlopen(foundation+question)
    html = response.read()

    extract_urls(html,question)

main_routine()
