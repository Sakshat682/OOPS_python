f = open('./read.txt', 'w') 
s = input("Enter what you want to write inside the file: ")
f.write(s)
f.close()
print("Writing complete\n")