# Калькулятор защищенности пароля

Скрипт оценивает защищенность пароля по следующим характеристикам:
- длина более 8 символов
- смешенный регистр
- наличие цифр
- наличие специальных знаков (!№%?@ и т.д.)
- не является часто используемым типа P@sword и т.д
Основываясь на данных факторах программа оценивает сложность пароля от 1 до 10
1 - слабый пароль, 10 - сильный пароль.

# Пример использования:
### (Ввод пароля скрыт)

Запуск на Linux:

```#!bash

python password_strength.py
Введите пароль для проверки:            
Защищенность вашего пароля - 10

```

Запуск на Windows происходит аналогично.


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
