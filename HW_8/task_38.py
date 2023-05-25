# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import csv

# Функция для загрузки данных из текстового файла
def load_data(file_name):
    directory = []
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                directory.append(row)
    except FileNotFoundError:
        print("Файл не найден. Создаем новый телефонный справочник.")
    return directory

# Функция сохранения данных в текстовый файл
def save_data(directory, file_name):
    with open(file_name, "w") as file:
        writer = csv.writer(file, delimiter=",")
        for record in directory:
            writer.writerow(record)
    print("Телефонный справочник успешно сохранен.")

# Функция отображения всех записей
def display_records(directory):
    if directory:
        for record in directory:
            print(" ".join(record))
    else:
        print("Телефонный справочник пуст.")

# Функция поиска записи по имени или фамилии
def search_record(directory, name):
    found = False
    for record in directory:
        if name.lower() in [part.lower() for part in record[:3]]:
            print(" ".join(record))
            found = True
    if not found:
        print("Соответствующая запись не найдена.")

# Функция для изменения записи по имени или фамилии
def modify_record(directory, name):
    modified = False
    for record in directory:
        if name.lower() in [part.lower() for part in record[:3]]:
            new_phone = input("Введите новый номер телефона:")
            record[3] = new_phone
            print("Запись успешно изменена.")
            modified = True
    if not modified:
        print("Соответствующая запись не найдена.")

# Функция удаления записи по имени или фамилии
def delete_record(directory, name):
    deleted = False
    for record in directory:
        if name.lower() in [part.lower() for part in record[:3]]:
            directory.remove(record)
            print("Запись успешно удалена.")
            deleted = True
    if not deleted:
        print("Соответствующая запись не найдена.")

# Функция для добавления контакта
def add_contact(directory):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите телефонный номер: ")
    new_contact = [last_name, first_name, patronymic, phone_number]
    directory.append(new_contact)
    print("Контакт успешно добавлен.")

def main():
    file_name = "phone_directory.txt"
    directory = load_data(file_name)

    while True:
        print("\nТелефонный справочник")
        print("1. Отобразить все записи")
        print("2. Найти запись")
        print("3. Изменить запись")
        print("4. Удалить запись")
        print("5. Добавить контакт")
        print("6. Сохранить и выйти")

        choice = input("Выберите пункт (1-6): ")
        if choice == "1":
            display_records(directory)
        elif choice == "2":
            search_name = input("Введите имя или фамилию для поиска: ")
            search_record(directory, search_name)
        elif choice == "3":
            modify_name = input("Введите имя или фамилию для изменения: ")
            modify_record(directory, modify_name)
        elif choice == "4":
            delete_name = input("Введите имя или фамилию для удаления: ")
            delete_record(directory, delete_name)
        elif choice == "5":
            add_contact(directory)
        elif choice == "6":
            save_data(directory, file_name)
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()