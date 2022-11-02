filee = open("dict.txt", "r", encoding="utf-8")
file2 = open("dict.txt", "a", encoding="utf-8")
lines = filee.readlines()
print(lines)
file2.truncate(0)
lines2 = []

for line in lines:
    line = line.upper()
    line = line.replace("\n", "")
    lines2.append(line)

lines = sorted(lines2)

for line in lines:
    line = line + "\n"
    file2.write(line)