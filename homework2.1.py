def total_salary(path):
    total_sum = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:

            for line in file:

                line = line.strip()

                parts = line.split(',')

                salary = int(parts[1])

                total_sum += salary

                count += 1



        if count > 0:
            average = total_sum / count
        else:
            average = 0


        return (total_sum, average)

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Інша помилка: {e}")
        return (0, 0)



total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")