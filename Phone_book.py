# Импорт модуля csv для работы с файлами CSV
import csv


# Функция для вывода на экран заданного количества записей из справочника, начиная с указанной страницы
def display_contacts(page_size, page_number):
    # Открытие файла 'contacts.csv' в режиме чтения
    with open('contacts.csv', 'r') as file:
        # Чтение содержимого файла и сохранение его в список contacts
        contacts = list(csv.reader(file))

        # Определение начального индекса записи
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size

        # Выборка нужных записей из списка contacts
        selected_contacts = contacts[start_index:end_index]

        # Вывод выбранных записей на экран
        for contact in selected_contacts:
            print(contact)


# Функция для добавления новой записи в файл CSV
def add_contact(last_name, first_name, middle_name, organization, work_phone, personal_phone):
    with open('contacts.csv', 'a') as file:
        # Создание объекта writer для записи данных в файл
        writer = csv.writer(file)

        # Запись переданной записи в файл
        writer.writerow([last_name, first_name, middle_name, organization, work_phone, personal_phone])


# Функция для редактирования существующей записи в файле CSV
def edit_contact(index, last_name, first_name, middle_name, organization, work_phone, personal_phone):
    with open('contacts.csv', 'r') as file:
        # Чтение содержимого файла и сохранение его в список contacts
        contacts = list(csv.reader(file))

        # Проверка валидности переданного индекса
        if index >= 0 and index < len(contacts):
            # Замена записи с указанным индексом на новую запись
            contacts[index] = [last_name, first_name, middle_name, organization, work_phone, personal_phone]

            with open('contacts.csv', 'w') as file:
                # Запись обновленных данных в файл
                writer = csv.writer(file)
                writer.writerows(contacts)


# Функция для поиска записей в файле CSV, которые соответствуют заданным характеристикам
def search_contacts(search_terms):
    with open('contacts.csv', 'r') as file:
        # Чтение содержимого файла и сохранение его в список contacts
        contacts = list(csv.reader(file))

        # Создание пустого списка matching_contacts для хранения найденных записей
        matching_contacts = []

        # Итерация по каждой записи в списке contacts
        for contact in contacts:
            # Проверка, содержатся ли все характеристики из списка search_terms в соответствующих полях записи
            if all(term in contact for term in search_terms):
                # Добавление записи в список matching_contacts
                matching_contacts.append(contact)

        # Вывод найденных записей на экран
        for contact in matching_contacts:
            print(contact)


# Бесконечный цикл while для предоставления пользователю выбора действий
while True:
    # Вывод списка действий на экран
    print("1. Вывести записи на экран")
    print("2. Добавить новую запись")
    print("3. Редактировать запись")
    print("4. Поиск записей")
    print("5. Выход")

    # Ввод выбранного действия
    action = int(input("Выберите действие: "))

    # Если выбрано действие "Вывести записи на экран"
    if action == 1:
        # Ввод размера страницы и номера страницы
        page_size = int(input("Введите размер страницы: "))
        page_number = int(input("Введите номер страницы: "))

        # Вызов функции display_contacts с заданными параметрами
        display_contacts(page_size, page_number)

    # Если выбрано действие "Добавить новую запись"
    elif action == 2:
        # Ввод фамилии, имени, отчества,названия организации, рабочего телефона и личного телефона
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        organization = input("Введите название организации: ")
        work_phone = input("Введите рабочий телефон: ")
        personal_phone = input("Введите личный телефон: ")

        # Вызов функции add_contact с заданными параметрами
        add_contact(last_name, first_name, middle_name, organization, work_phone, personal_phone)

    # Если выбрано действие "Редактировать запись"
    elif action == 3:
        # Ввод индекса записи, которую нужно отредактировать
        index = int(input("Введите индекс записи: "))

        # Ввод новой фамилии, имени, отчества, названия организации, рабочего телефона и личного телефона
        last_name = input("Введите новую фамилию: ")
        first_name = input("Введите новое имя: ")
        middle_name = input("Введите новое отчество: ")
        organization = input("Введите новое название организации: ")
        work_phone = input("Введите новый рабочий телефон: ")
        personal_phone = input("Введите новый личный телефон: ")

        # Вызов функции edit_contact с заданными параметрами
        edit_contact(index, last_name, first_name, middle_name, organization, work_phone, personal_phone)

    # Если выбрано действие "Поиск записей"
    elif action == 4:
        # Ввод характеристик для поиска, разделенных запятыми
        search_terms = input("Введите характеристики для поиска: ").split(',')

        # Вызов функции search_contacts с заданными характеристиками
        search_contacts(search_terms)

    # Если выбрано действие "Выход"
    elif action == 5:
        # Прерывание цикла while и завершение программы
        break