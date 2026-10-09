file=open("abc.txt", "r")
count=0
content=file.read()
colist=content.split("\n")

for i in colist:
    count+=1
print("Number of lines in the file:", count)
file.close()