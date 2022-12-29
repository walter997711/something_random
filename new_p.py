from os import system
def print_current_dir():
    return print(system("ls"))

print("do u want to a >> 0pen r4ndom file:")
a=input("do you want to list of files in current dir:[y/n]").lower()
if a=="y" or a=="yes":
    print_current_dir()

n_f=input("file_name: ")
random_file=open(n_f,"r")
print(random.file.readlines())
