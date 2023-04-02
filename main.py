import os
import tkinter as tk
import subprocess

root = tk.Tk()
root.title('Retro Realm')
root.geometry('1040x800')
root.configure(bg='cyan')


cwd = os.getcwd()

welcome_text = tk.Label(root, text='Retro Realm', font=("Arial", 60, 'bold'), bg = "cyan")
welcome_text.grid(row=0, column=0, columnspan=5, pady = 30)

desc = tk.Label(root, text='Retro Realm is a catalog of classic games: choose your game above.', font=("Arial", 24), bg="cyan")
desc.grid(row=4, column = 0, columnspan=5)


game_files = os.listdir(cwd)
row_num = 1
col_num = 0

for game in game_files:
    if ".py" not in game:
        button = tk.Button(root, text=game, command=lambda game=game: run_game(game), width = 20, height = 5)
        button.grid(row=row_num, column = col_num, padx = 10, pady = 10)
        col_num += 1
        if col_num == 5:
            col_num = 0
            row_num += 1

root.columnconfigure(0, weight=1)
root.columnconfigure(6, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(row_num+1, weight=1)

def run_game(game):
    os.chdir(cwd)
    game_dir = os.path.join(cwd, game)
    os.chdir(game_dir)
    subprocess.run(["python3", "main.py"])
root.mainloop()

