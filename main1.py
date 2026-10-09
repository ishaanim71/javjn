file_read=open("abc.txt", "r")
print("File in read mode:")
print(file_read.read())
file_read.close()

file_write=open("abc.txt", "w")
print("File in write mode:")
file_write.write("himynameisishaaniliketurtlestheyareawesome")
file_write.close()

file_append=open("abc.txt", "a")
print("File in append mode:")
file_append.write("\nI am adding this line to the file.")
file_append.close()