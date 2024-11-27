import wikipedia

wikipedia.set_lang("ru")

def search_wikipedia():
    print("Добро пожаловать в Википедию через консоль!")
    while True:
        query = input("\nВведите запрос для поиска на Википедии (или 'выход' для завершения): ")
        if query.lower() == "выход":
            print("Выход из программы")
            break

        try:
            page = wikipedia.page(query)
            print(f"\nСтатья найдена: {page.title}\n")

            while True:
                print("Что вы хотите сделать?")
                print("1. Листать параграфы текущей статьи")
                print("2. Перейти на одну из внутренних страниц")
                print("3. Выйти в главное меню")
                action = input("Введите номер действия: ")

                if action == "1":
                    paragraphs = page.content.split("\n")
                    for i, paragraph in enumerate(paragraphs, start=1):
                        print(f"\nПараграф {i}:\n{paragraph}\n")
                        next_action = input("Введите 'далее' для следующего параграфа или 'стоп' для остановки: ")
                        if next_action.lower() == "стоп":
                            break

                elif action == "2":
                    print("\nСвязанные страницы:")
                    links = page.links[:10]  # Ограничиваем количество ссылок для удобства
                    for i, link in enumerate(links, start=1):
                        print(f"{i}. {link}")

                    choice = input("\nВведите номер страницы для перехода или 'назад' для возврата: ")
                    if choice.lower() == "назад":
                        continue

                    try:
                        choice = int(choice) - 1
                        if 0 <= choice < len(links):
                            page = wikipedia.page(links[choice])
                            print(f"\nПереход на страницу: {page.title}")
                        else:
                            print("Некорректный выбор. Попробуйте снова.")
                    except ValueError:
                        print("Некорректный ввод. Введите номер страницы или 'назад'.")

                elif action == "3":
                    print("Возврат в главное меню.")
                    break

                else:
                    print("Некорректный выбор. Попробуйте снова.")

        except wikipedia.exceptions.DisambiguationError as e:
            print("\nВаш запрос неоднозначен. Возможные варианты:")
            for option in e.options[:10]:  # Ограничиваем до 10 вариантов
                print(option)
            print("Попробуйте уточнить запрос.")
        except wikipedia.exceptions.PageError:
            print("\nСтатья не найдена. Попробуйте другой запрос.")
        except Exception as ex:
            print(f"\nПроизошла ошибка: {ex}. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    search_wikipedia()