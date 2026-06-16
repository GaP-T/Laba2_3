target_word = input("Введите слово для поиска: ")

found_lines = []
total_count = 0

file = open('text.txt', 'r', encoding='utf-8')
current_line_number = 1

for line in file:
    count_in_line = line.count(target_word)

    if count_in_line > 0:
        total_count = total_count + count_in_line
        found_lines.append(current_line_number)

    current_line_number = current_line_number + 1
file.close()

if total_count > 0:
    is_found_text = "Да"
else:
    is_found_text = "Нет"

print("Результаты поиска:")
print("Слово найдено:", is_found_text)

if total_count > 0:
    print("Сколько раз встречается:", total_count)
    print("Номера строк:", found_lines)

out = open('search_results.txt', 'w', encoding='utf-8')

out.write("Слово: " + target_word + "\n")
out.write("Найдено: " + is_found_text + "\n")

if total_count > 0:
    lines_as_text = str(found_lines)
    out.write("Количество: " + str(total_count) + "\n")
    out.write("Строки: " + lines_as_text + "\n")

out.close()
