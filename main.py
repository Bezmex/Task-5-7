from menu_functions import f1, f2, f3
from functions_for_work import is_int

def menu():
    result = []
    text_input = False
    algoritm_done = False

    while 1:
        print("Выберите пункт меню:\n"
              "1. Ввод исходного текста \n"
              "2. Выполнение алгоритма по поиску палиндромов в тексте\n"
              "3. Вывод результата\n"
              "4. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)

        if choice == 1:
            text_input = f1()

        elif choice == 2:
            if text_input:
                result = f2()
                algoritm_done = True
            else:
                print("Ошибка!\nСначала введите текст\n\n")
        elif choice == 3:
            if algoritm_done:
                if text_input:
                    f3(result)
            else:
                print("\nСначала выполните алгоритм\n")
        elif choice == 4:
            break
        else:
            print('error')

if __name__ == "__main__":
    menu()