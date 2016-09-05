import sys
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

    if len(urls) > 0:
        return random.choice(urls)

    return -1

def extract_urls(html,question):
    folder =  "C:\\Users\\Dimitris\\Desktop\\DeviantArt\\"+question

    url = random_html_image(html)
    if url == -1:
            return -1

    name = url.split('/')[-1]

    if not os.path.isdir(folder):
        print folder
        os.mkdir(folder)

    fetch_url(url, folder+"/"+name)

def generate_questions():

    terms = []
    with open("C:\\Users\\Dimitris\\Desktop\\DeviantArt\\Terms.txt") as f:
        for line in f:
            line = line.replace("\n","")
            terms.append(line)

    return random.choice(terms)

def main_routine():
    foundation = "http://www.deviantart.com/browse/all/?q="
    question = generate_questions()

    n = random.randint(0, 10000)
    response = urllib.urlopen(foundation+question+"&offset="+str(n))
    html = response.read()

    extract_urls(html, question)

a = sys.argv[1]
for i in range(int(a)):
    	main_routine()
