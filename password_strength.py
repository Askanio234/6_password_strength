import sys


common_words = "hello, world, guest, password, user"

common_passwords = ("password1, welcome1, p@ssword, summer1!, fa$hion1, "
                    "hello123, welcome123, 123456q@, p@ssword1")

unaceptable_passwords = common_words + " " + common_passwords


def analyze_password_length(password):
    result = 0
    if len(password) > 8:
        return 3
    elif 4 < len(password) <= 8:
        return 2
    else:
        return 1


def analyze_presense_of_digits(password):
    if any([character.isdigit() for character in password]):
        return 2
    else:
        return 0


def analyze_presense_of_mixed_case(password):
    if any(
        [character.isupper() for character in password]
        ) and any(
        [character.islower() for character in password]
        ):
        return 2
    else:
        return 0


def analyze_presense_of_special_symbols(password):
    if any([not character.isalnum() for character in password]):
        return 2
    else:
        return 0


def get_password_strength(password):
    result = 1
    if not password.lower() in unaceptable_passwords:
        result += (analyze_password_length(password)
                    + analyze_presense_of_digits(password)
                    + analyze_presense_of_mixed_case(password)
                    + analyze_presense_of_special_symbols(password))
        return result
    else:
        return result


if __name__ == '__main__':
    password = input("Введите пароль для проверки: ")
    if password:
        print(get_password_strength(password))
    else:
        print("Некорректный ввод")
