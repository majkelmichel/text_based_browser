import os
from sys import argv
from collections import deque
import requests

args = argv

if len(args) != 2:
    print("Wrong number of arguments")

directory = args[1]
stack = deque()

try:
    os.mkdir(directory)
except FileExistsError:
    pass

# print(os.getcwd())
# os.chdir('../')
# print(os.path.dirname(os.getcwd()))

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


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


while True:
    url = input()
    path_no_dot = directory + "/" + url
    if url == "back":
        stack.pop()
        url = stack[len(stack) - 1]
    elif url == "exit":
        print('error')
        break
    if os.path.isfile(path_no_dot):
        stack.append(url)
        with open(path_no_dot) as file:
            print(file.read())
    elif check_url(url):
        stack.append(url)
        path_with_dot = directory + "/" + delete_dot(url)
        url = check_for_https(url)
        req = requests.get(url)
        with open(path_with_dot, 'w', encoding='utf-8') as file:
            file.write(req.text)
    else:
        print("error: wrong URL")