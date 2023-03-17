import sys


def greet(name):
    print('Hello, {}!'.format(name))


if len(sys.argv) > 1:
    name = sys.argv[1] # sys.argv는 명령줄 매개변수를 나타내는 리스트 형식의 변수임.
    greet(name)

else:
    greet('world')