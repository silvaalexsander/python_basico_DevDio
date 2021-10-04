class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        num = int(input('Insira um numero entre 0 e 10: '))
        if num > 10 or num < 0:
            raise InputError('Numero apenas entre 0 e 10')
        break
    except ValueError:
        print(f'Favor digitar um numero inteiro entre 0 e 10 ')
    except InputError as ex:
        print(ex)