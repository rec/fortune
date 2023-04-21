import subprocess

KWARGS = {'text': True, 'stdout': subprocess.PIPE}
MAX_LEN = 500


def get_fortune():
    while len(f := subprocess.run('fortune', **KWARGS).stdout) > MAX_LEN:
        pass
    return f


print(get_fortune(), end='')
