files = ["file1.txt", "file2.txt", "file3.txt"]
with open('combined.txt', 'w', encoding='utf-8') as output:
    for file in files:
        with open(file, "r", encoding="utf-8") as infile:
            output.write(infile.read())
            output.write("\n\n")