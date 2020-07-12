import os
from sys import argv
from collections import deque
import requests
from bs4 import BeautifulSoup

args = argv

if len(args) != 2:
    print("Wrong number of arguments")

directory = args[1]
stack = deque()

try:
    os.mkdir(directory)
except FileExistsError:
    pass


# write your code here


def check_url(url_to_check):
    return '.' in set(url_to_check)


def delete_dot(url_to_modify):
    new_url = list(url_to_modify[::-1])
    return "".join(new_url[:new_url.index('.'):-1])


def check_for_https(url_string):
    if url_string.startswith("https://"):
        return url_string
    return f'https://{url_string}'


def get_text_from_page(page):
    soup = BeautifulSoup(page, "html.parser")
    tags_list = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'a', 'ul', 'ol', 'li']
    return soup.find_all(tags_list)


while True:
    url = input()
    path_no_dot = directory + "/" + url
    if url == "back":
        stack.pop()
        url = stack[len(stack) - 1]
    if url == "exit":
        break
    elif os.path.isfile(path_no_dot):
        stack.append(url)
        with open(path_no_dot) as file:
            print(file.read())
    elif check_url(url):
        stack.append(url)
        path_with_dot = directory + "/" + delete_dot(url)
        url = check_for_https(url)
        req = requests.get(url)
        scraped = get_text_from_page(req.content)
        with open(path_with_dot, 'w', encoding='utf-8') as file:
            for tag in scraped:
                file.write(tag.get_text())
                print(tag.get_text())

    else:
        print("error: wrong URL")
