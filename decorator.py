def logger(path='C:\\Users\\user\Desktop'):
    from datetime import datetime

    def _logger(func):
        def log_func(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            with open(f'{path}\\log {func.__name__}.txt', 'w') as file:
                file.write(f'Дата и время вызова функции: {start}\n'
                           f'Имя функции: {func.__name__}\n'
                           f'Аргументы функции: {args} {kwargs}\n'
                           f'Результат функции: {result}')
            return result
        return log_func
    return _logger


@logger()
def sum(a, b):
    return a + b


sum(5, 7)

