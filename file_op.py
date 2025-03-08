import os
with open("fruit.txt","w") as f:
    f.write("I ate strawberry today")

# Extracting words 
with open("fruit.txt","r") as f:
    line = f.readlines()
    for m in line:
        word = m.split()
        print(word)

os.remove("fruit.txt")
os.rmdir("delete_1")

