def user_info(first_name: str, second_name: str, birth_year: int, city: str, email: str, phone: str) -> str:
    """ Функция вывода информации о пользователях
    """
    return f'{first_name} {second_name} {birth_year} {city} {email} {phone}'


if __name__ == "__main__":
    print(user_info(first_name='David', second_name='Chulakov', birth_year=2002, city='Moscow',
                    email='daweedxinfo@gmail.com', phone='+79777777777'))
    print(user_info(first_name='Oleg', second_name='Tinkov', birth_year=1970, city='Moscow',
                    email='email@gmail.com', phone='+79222222222'))