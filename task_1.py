with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

line_count = len(lines)
word_count = len(" ".join(lines).split())

with open('statistics.txt', 'w', encoding='utf-8') as f:
    f.write(f"количество строк: {line_count}\n")
    f.write(f"количество слов: {word_count}\n")
print("сохранено :)")
