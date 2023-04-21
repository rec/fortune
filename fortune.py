from functools import cache
from mastodon import Mastodon
import subprocess
import time


KWARGS = {'text': True, 'stdout': subprocess.PIPE}
MAX_LEN = 500
ACCESS_TOKEN = open('access-token.txt').read().strip()
BASE_URL = 'https://botsin.space/'
DELAY = 3600


@cache
def mastodon():
    return Mastodon(
        access_token = ACCESS_TOKEN,
        api_base_url = 'https://botsin.space/'
    )


def get_fortune():
    while len(f := subprocess.run('fortune', **KWARGS).stdout) > MAX_LEN:
        pass
    return f


def main():
    while True:
        f = get_fortune()
        print(f)
        mastodon().status_post(f)

        time.sleep(DELAY)


if __name__ == '__main__':
    main()
