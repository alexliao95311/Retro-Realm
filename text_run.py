import os
import subprocess
cwd = os.getcwd()


def run_game():
    new_cwd = os.getcwd()

    subprocess.run(['python3', f'{new_cwd}/main.py'])


print('''
Welcome to Retro Realm!
Choose your game!
1. Asteroids
2. Pong
3. Space Invaders
4. Tetris
5. Flappy Bird
6. Tic Tac Toe
7. Connect Four
8. Snake
9. Chess
10. Traffic
''')

game = int(input('Enter your choice number: '))

if game == 1:
    os.chdir(f'{cwd}/Asteroids')
    run_game()
elif game == 2:
    os.chdir(f'{cwd}/Pong')
    run_game()
elif game == 3:
    os.chdir(f'{cwd}/SpaceInvaders')
    run_game()
elif game == 4:
    os.chdir(f'{cwd}/Tetris')
    run_game()
elif game == 5:
    os.chdir(f'{cwd}/FlappyBird')
    run_game()
elif game == 6:
    os.chdir(f'{cwd}/TicTacToe')
    run_game()
elif game == 7:
    os.chdir(f'{cwd}/ConnectFour')
    run_game()
elif game == 8:
    os.chdir(f'{cwd}/Snake')
    run_game()
elif game == 9:
    os.chdir(f'{cwd}/Chess')
    run_game()
elif game == 10:
    os.chdir(f"{cwd}/Traffic")
    run_game()
