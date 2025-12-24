def get_cats_info(path):
    cats_list = []

    try:

        with open(path, 'r', encoding='utf-8') as file:


            for line in file:

                line = line.strip()

                parts = line.split(',')

                cat_dict = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats_list.append(cat_dict)


    except FileNotFoundError:
        return "Файл не знайдено. Перевірте шлях."
    except Exception as e:
        return f"Сталася помилка: {e}"

    return cats_list
cats_info = get_cats_info("cats.txt")
print(cats_info)