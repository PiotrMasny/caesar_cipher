import os
from datetime import datetime as dt
from string import ascii_lowercase as alphabet

from ciphers.caeser import CaesarCipher
from utils.files import FileManager
from utils.history import Record


class Facade:
    filename = "history.json"

    def __init__(self):
        self.choices = {
            "1": self.encrypt_text,
            "2": self.decrypt_text,
            "3": self.save_to_file,
            "4": self.view_history,
            "9": self.close_app,
        }
        self.__is_running = True
        self.__is_saved = True
        self.memory = []
        self.cipher = CaesarCipher(alphabet)
        self.files = FileManager()

    def loop(self):
        while self.__is_running:
            try:
                self.show_menu()
                user_choice = input("")
                self.choices.get(user_choice)()
            except TypeError:
                self.show_error()

    def show_menu(self):
        os.system("cls")
        print("\n Choose an option:")
        for key, value in self.choices.items():
            print(f"{key}: {value.__name__}")
        print()

    def encrypt_text(self):
        try:
            user_message = input("Enter message to encrypt\n")
            user_key = int(input("Enter a key value: "))
            self.key_validation(user_key)
            encrypted_message = self.cipher.encrypt(user_message, user_key)
            print("Encrypted message: ", encrypted_message)

            self.memory.append(
                Record(
                    date=str(dt.now()),
                    user_message=user_message,
                    user_key=user_key,
                    encrypted_message=encrypted_message,
                    decrypted_message=None,
                )
            )
            self.__is_saved = False
        except ValueError:
            self.show_error()

    def decrypt_text(self):
        try:
            user_message = input("Enter message to decrypt\n")
            user_key = int(input("Enter a key value: "))
            self.key_validation(user_key)
            decrypted_message = self.cipher.decrypt(user_message, user_key)
            print("Decrypted message: ", decrypted_message)
            self.memory.append(
                Record(
                    date=str(dt.now()),
                    user_message=user_message,
                    user_key=user_key,
                    encrypted_message=None,
                    decrypted_message=decrypted_message,
                )
            )
            self.__is_saved = False
        except ValueError:
            self.show_error()

    @staticmethod
    def key_validation(key: int):
        if key < 0:
            raise ValueError

    def save_to_file(self):
        self.files.save_to_file(self.memory)
        self.__is_saved = True

    def view_history(self):
        self.files.view_history(self.memory)

    def close_app(self):
        if not self.__is_saved:
            user_decision = input(
                "You have unsaved history, " "do you want to save? [y/n]: "
            )
            if user_decision.lower() == "y":
                self.save_to_file()
                self.__is_running = False
                print("Closing app")
            elif user_decision.lower() == "n":
                self.__is_running = False
                print("Closing app")
            else:
                self.show_error()
                self.close_app()

    @staticmethod
    def show_error():
        print("Invalid value")
