
with open("text.txt", "r") as f:
    text = f.read()

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

with open("report.txt", "w") as f:
    for word in word_count:
        f.write(word + ": " + str(word_count[word]) + "\n")

print("Report created successfully")




# hello this is my second commit