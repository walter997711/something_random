from imgtoascii import imgtoascii
fl_name=input("give us a file name: ")
# Example:1
#imgtoascii(fl_name).view()
# Example:2
p1=imgtoascii(fl_name,False).view()
for i in range(len(p1)):
    print(p1[i])
