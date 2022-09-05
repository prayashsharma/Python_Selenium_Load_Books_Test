import json
from book import Book
from add_books import *

BASE_URL = "http://localhost:3000/books/new"


def map_dictionary_to_object(data):
    list_of_books = json.loads(json.dumps(
        data), object_hook=lambda d: Book(**d))
    return list_of_books


def read_json_data_from_file():
    with open('input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def process_data(data):
    for book in data:
        add_books_using_chrome_browser(BASE_URL, book)


def main():
    data = read_json_data_from_file()
    list_of_books = map_dictionary_to_object(data)
    process_data(list_of_books)


if __name__ == "__main__":
    main()
