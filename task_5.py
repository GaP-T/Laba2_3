try:
    with open("words.txt", "r", encoding="utf-8") as infile:
        words = []
        for line in infile:
            words.append(line.strip())

    words_alfavit = sorted(words)
    words_length = sorted(words, key=len)
    words_reverse = sorted(words, reverse=True)

    with open("orted_alphabetically.txt", "w", encoding="utf-8") as outfile:
        outfile.writelines(f"{word}\n" for word in words_alfavit)

    with open("sorted_by_length.txt", "w", encoding="utf-8") as outfile:
        outfile.writelines(f"{word}\n" for word in words_length)

    with open("sorted_reverse.txt", "w", encoding="utf-8") as outfile:
        outfile.writelines(f"{word}\n" for word in words_reverse)

    print("Файлы созданы успешно")

except FileNotFoundError:
    print("Ошибка: Файл words.txt не найден")
except OSError:
    print("Ошибка при работе с файлами")
