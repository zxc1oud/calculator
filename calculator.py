# Проект 1 из 100

import re

while True:
    print(r"Привет! я - скрипт-калькулятор. Напиши свой пример используя доступные операторы (+, -, //, *, /, **, %)")
    expression = input("Вводи свой пример сюда: ")
    
    if not re.fullmatch(r"[\d+\-*/%()]+", expression):
        print("Операторы в этом примере не соответствуют требованию скрипта.")
        continue
    
    response = eval(expression)
    print(
        f"Я решил этот пример, вот что у меня получилось:\n"
        f"{expression}={response}\n"
        f"Ответ: {response}"
    )
    
    question = input("Вы хотите продолжить? (Y/N): ").lower()
    if question.lower() == "y":
        continue
    elif question.lower() == "n":
        break
    else:
        print("Ошибка!")
        break