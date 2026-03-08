lines = []

print("Enter lines of text. Type 'done' to finish.\n")

while True:
    line = input()
    if line.lower() == "done":
        break
    lines.append(line)

print("\nOutput:")
for index, line in enumerate(lines, start=1):
    print(f"{index}. {line}")
