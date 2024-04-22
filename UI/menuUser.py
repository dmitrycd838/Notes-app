import UI.menuHeader as m


def menu_console():
        m.printMenuTitle("Заметки\n           главное меню")
        print("1 - вывод журнала \n2 - вывод заметки по id \n3 - выбор заметки по дате \n4 - редактирование заметки"
              " \n5 - добавление заметки \n6 - удаление заметки \n7 - выход из заметок")
        m.printMenuLine()
        print("\n выберите пункт из меню ")