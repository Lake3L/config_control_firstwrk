import os
import platform

class Shell:
    def __init__(self): #
        self.running = True

    def get_prompt(self):
        username = os.getlogin()
        hostname = platform.node()
        invite = f"{username}@{hostname}:~$ " #2 этап
        return invite

    def parser_input(self, input_string): #3 этап
        parser = input_string.strip().split()
        command = parser[0]
        args = parser[1:]
        return command, args
    
    def func():
        print("SSSStestSSSS")
        
    def execute_command(self, command, args):
        if command == "exit":
            self.running = False
            print("Выход из эмулятора.")
        
        elif command == "ls":
            print(f"Команда: ls, Аргументы: {args}")

        elif command == "cd":
            print(f"Команда: cd, Аргументы: {args}")

        else: print(f"Неизвестная команда {command}")

    def run(self):
        while self.running:
            user_input = input(self.get_prompt()) #Ввод
            command, args = self.parser_input(user_input) #Парсинг ввода
            self.execute_command(command, args) #запуск обработчика комманд

if __name__ == "__main__":
    shell = Shell()
    shell.run()
