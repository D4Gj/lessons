user_permissions = ['user']


def check_permissions(permission):
    def wrapper_permission(func):
        def wrapped_check():
            if permission not in user_permissions:
                raise ValueError("Недостаточно прав")
            return func()

        return wrapped_check

    return wrapper_permission


@check_permissions('user')
def check_value():
    return 'какие-то данные'


@check_permissions('admin')
def change_smtng():
    return 'Действия админа'


print('start')
check_value()
# change_smtng()
print('end')
