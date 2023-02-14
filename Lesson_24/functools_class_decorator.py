def singleton(cls):
    """Класс Singleton (один экземпляр)"""

    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, *kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class OriginalWorker:
    pass

print('start')
first_one = OriginalWorker()
second_one = OriginalWorker()
print(id(first_one))
print(id(second_one))
print('конец')
