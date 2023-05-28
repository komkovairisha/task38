def new_rec(mode="new") -> tuple:
    if mode == "new":
        print("Режим ввода новой записи ")
    elif mode == "update":
        print("Ввод новых данных для записи {surname}")
        print("Пустая строка означает: оставить данные без изменения")
    else:
        raise ValueError(f"Недопустимое значение mode: {mode}")
    surname = input("Введите фамилию: ")
    name = input("Введите имя отчество: ")
    tel = input("Введите номер телефона: ")
    desc = input("Введите описание: ")
    return surname, name, tel, desc

def surname():
    return input("Введите фамилию: ")

def show_recs(recs: list):
    for rec in recs:
        show_rec(rec)

def show_rec(rec: dict):
    for val in rec.values():
        print(val, end=" ")
    print("")

def show_all_recs(phone_book: list):
    print("Cправочник: ")
    for rec in phone_book:
        show_rec(rec)

def show_menu() -> str:
    print("_"*55)
    print("\n\tМЕНЮ:")
    print("\t(1)create - Ввод новой записи:")
    print("\t(2)read   - Поиск записи по фамилии")
    print("\t(3)udate  - Изменение записи по фамилии")
    print("\t(4)delete - Удаление записи по фамилии")
    print("\t(5)show   - Просмотр телефонного справочника \n")
    return input("Выберите нужный пункт: ")