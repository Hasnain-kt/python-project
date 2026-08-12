# word = input()

# new_content=[]
# with open("demo.txt" , "r") as f:
#     for x in f:
#         y = x.strip()
#         if word != y:
#             new_content.append(y)

# with open("demo.txt" , "w") as f:
#     text = "\n".join(new_content)
#     f.write(text)        

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