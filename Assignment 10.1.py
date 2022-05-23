import os.path


def main():
    path = input("Enter the directory you wish to create a file (absolute path): ")
    if(os.path.isdir(path)):
        print("This directory exists.")
        file_name = input("Enter the name of the file you wish to create: ")
        name = input("Enter your name: ")
        addr = input("Enter your address: ")
        phone_num = input("Enter your phone number: ")
        with open(file_name, 'w') as fp:
            fp.write("%s,%s,%s\n" %(name, addr, phone_num))
        file_path = path + '/' + file_name
        print(file_path)
        with open(file_path, 'r') as fp:
            pf = fp.read()
            print(pf)
    else:
        print("This directory does not exist.")



if __name__ == "__main__":
    main()