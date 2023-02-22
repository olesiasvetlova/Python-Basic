def password_required(func):
    """
    Функція  яка буде запитувати у користувача пароль перед викликом інших функцій.
    Якщо пароль вірний, то секретні дані виводяться на екран.
    :param func:
    :return: password verification
    """
    def wraper():
        password = 'admin'
        ent_paswrd = input('Enter password: ')
        if password == ent_paswrd:
            func()
        else:
            print('Password is wrong')
    return wraper


@password_required
def bank_credentials():
    print("Bank card: 0000-1111-2222-3333-4444")
    print("Bank password: 1234")
    print("amount: 100 000 000$")


@password_required
def instagram_credentials():
    print("username: snowden")
    print("password: cia")


bank_credentials()
instagram_credentials()