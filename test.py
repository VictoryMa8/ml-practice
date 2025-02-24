import shutil

def joe_mama():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("Joe Mama!")
        elif i % 3 == 0:
            print("Joe")
        elif i % 5 == 0:
            print("Mama")
        else:
            print(i)

def main():
    shutil.move("./test.txt", "./test_folder")

if __name__ == "__main__":
    main()