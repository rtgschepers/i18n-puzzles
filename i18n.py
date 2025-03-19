import argparse
import webbrowser
from pathlib import Path

import requests


def main():
    parser = argparse.ArgumentParser(description='i18n puzzles management command.')
    parser.add_argument('puzzle', help='Number of the puzzle, e.g. 5 ',
                        choices=generate_days(), metavar='puzzle')
    parser.add_argument('-o', '--open', action='store_true', help='Open the selected puzzle in the browser')
    args = parser.parse_args()
    create_new_puzzle_files(args.puzzle, args.open)


def generate_days():
    return [str(x) for x in range(1, 21)]


def create_new_puzzle_files(puzzle, open_browser):
    url = f'https://i18n-puzzles.com/puzzle/{puzzle}'

    if open_browser:
        webbrowser.open(url, new=0, autoraise=True)

    folder = f'./Puzzle{int(puzzle):02d}'
    Path(folder).mkdir(parents=True, exist_ok=True)

    file_path = f'{folder}/puzzle.py'
    if not Path(file_path).is_file():
        with open('template.txt', 'r') as tpl:
            with open(file_path, 'w') as f:
                f.write(tpl.read())

    file_path = f'{folder}/test.txt'
    if not Path(file_path).is_file():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(get_test_input(url))

    file_path = f'{folder}/input.txt'
    if not Path(file_path).is_file():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(get_puzzle_input(url))


def send_request(url):
    from config import SESSION
    cookies = {'sessionid': SESSION}
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    response = requests.get(url, cookies=cookies, headers=headers)
    return response.text.strip()


def get_puzzle_input(url):
    return send_request(f'{url}/input')


def get_test_input(url):
    return send_request(f'{url}/test-input')


if __name__ == '__main__':
    main()
