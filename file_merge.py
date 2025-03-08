# File 1 
with open("file1.txt","r") as f1:
    data1 = f1.read()

# File 2
with open("file2.txt","r") as f2:
    data2 = f2.read()

# Merging files
data1 += "\n" #adding a new line after file1 data
data1 += data2

with open("MergedFile.txt","w") as f:
    f.write(data1)




