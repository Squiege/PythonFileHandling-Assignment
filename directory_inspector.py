# Task 1
import os

print("Please select a directory that you would like to view.")
print("1. Flowers")
print("2. Video Games")
print("3. Computer Parts")
user_directory = input("Please enter a directory that you would like to view (1-4): ")


def list_directory_contents(path):
    try:
        with open(path, "r") as file:
            selected_file = file.read()
            print(selected_file)
    except:
        pass

def main():
    while True:
        if user_directory == '1':
            list_directory_contents("flowers.txt")
        elif user_directory == '2':
            list_directory_contents("video_games.txt")
        elif user_directory == '3':
            list_directory_contents("computer_parts.txt")
        else:
            print("Invalid Choice.")

main()