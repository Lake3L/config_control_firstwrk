import argparse
import os
import platform
import tomli
from pathlib import Path

class Shell: # Этап 1
    def __init__(self): 
        self.running = True


    def get_prompt(self):
        username = os.getlogin()
        hostname = platform.node()
        invite = f"{username}@{hostname}:~$: " # 2 пункт
        return invite

    def parser_input(self, input_string): # 3 пункт
        parser = input_string.strip().split()
        command = parser[0]
        args = parser[1:]
        return command, args
    
    def dopdop():
        print("dopdop")
        
    def execute_command(self, command, args):
        if command == "exit":# 6 пункт
            self.running = False
            print("Выход из эмулятора.")
        
        elif command == "ls": # 5 пункт ##далее здесь путь к файловой системе
            print(f"Команда: ls, Аргументы: {args}")

        elif command == "cd":
            print(f"Команда: cd, Аргументы: {args}")

        else: print(f"Неизвестная команда {command}") # 4 пункт

    def run(self): # Основная функция запуска
        while self.running:
            user_input = input(self.get_prompt()) # Ввод
            command, args = self.parser_input(user_input) # Парсинг ввода
            self.execute_command(command, args) # Запуск обработчика комманд

if __name__ == "__main__":
    shell = Shell()
    shell.run()
