file1=input("Enter the first file name: ")
file2=input("Enter the second file name: ")

def swapFileData(file1,file2):
    try:
        with open(file1, 'r') as a:
            data_a = a.read()

        with open(file2, 'r') as a:
            data_b = a.read()


        with open(file1, 'w') as a:
            a.write(data_b)
            a.close()

        with open(file2, 'w') as a:
            a.write(data_a)
            a.close()

    except FileNotFoundError:
        print("No such files found!")

swapFileData(file1,file2)