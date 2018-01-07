import requests




def get_posts():
    r = requests.get('http://jsonplaceholder.typicode.com/posts')
    return r


def get_n_post(n):
    r = requests.get('http://jsonplaceholder.typicode.com/posts/' + n)
    return r
