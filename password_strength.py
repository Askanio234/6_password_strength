import sys
import getpass


UNACEPTABLE_PASSWORDS = {
                        "password1", "welcome1", "p@ssword", "summer1!",
                        "fa$hion1", "hello123", "welcome123", "123456q@",
                        "p@ssword1", "hello", "world", "guest", "password",
                        "user"
                        }


MIN_STENGTH = 1

MAX_STRENGTH = 10


def is_password_long(password):
    result = 0
    if len(password) > 8:
        return True
    else:
        return False


def is_digits_in_password(password):
    return any([character.isdigit() for character in password])


def is_mixed_case_in_password(password):
    return any(
        [character.isupper() for character in password]
        ) and any(
        [character.islower() for character in password]
        )


def is_special_symbols_in_password(password):
    return any([not character.isalnum() for character in password])


def get_password_strength(password):
    criterion = {
                is_password_long, is_digits_in_password,
                is_special_symbols_in_password, is_mixed_case_in_password
                }

    points_per_criteria = (MAX_STRENGTH - MIN_STENGTH)/len(criterion)

    if not password.lower() in UNACEPTABLE_PASSWORDS:
        return MIN_STENGTH + int(sum(
            [points_per_criteria if criteria(password) else 0 for criteria in criterion]
            ))
    else:
        return MIN_STENGTH


if __name__ == '__main__':
    password = getpass.getpass(prompt="Введите пароль для проверки: ")
    if password:
        print("Защищенность вашего пароля - {}".format(
            get_password_strength(password)
            ))
    else:
        print("Некорректный ввод")
