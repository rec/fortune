from functools import cache
from mastodon import Mastodon
import subprocess
import time
import traceback


KWARGS = {'text': True, 'stdout': subprocess.PIPE}
MAX_LEN = 500
ACCESS_TOKEN = open('access-token.txt').read().strip()
BASE_URL = 'https://botsin.space/'
DELAY = 3601
TAGS = """
#humor #unix #usr #games #fortune"""
MSG_LEN = MAX_LEN - len(TAGS)


def mastodon():
    return Mastodon(
        access_token = ACCESS_TOKEN,
        api_base_url = 'https://botsin.space/'
    )


def get_fortune():
    while len(f := subprocess.run('fortune', **KWARGS).stdout) > MSG_LEN:
        print('...Too long!', len(f))

    return f


def main():
    while True:
        time.sleep(DELAY)
        f = get_fortune()
        print('\n' + f + TAGS)
        try:
            mastodon().status_post(f + TAGS)
        except Exception:
            traceback.print_exc()


if __name__ == '__main__':
    main()
