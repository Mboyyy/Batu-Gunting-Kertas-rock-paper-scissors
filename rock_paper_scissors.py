import random

user_wins = 0
mboy_wins = 0

options = ["batu", "gunting", "kertas", "test"]

while True:
    user_input = input("Type Batu/Kertas/Gunting atau ketik Q untuk keluar.").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # batu: 0, kertas: 1, gunting: 2
    mboy_pick = options[random_number]
    print("Mboy picked", mboy_pick + ".")

    if user_input == "batu" or mboy_pick == "gunting":
        print("Kamu menang!")
        user_wins += 1

    elif user_input == "kertas" or mboy_pick == "batu":
        print("kamu menang!")
        user_wins += 1

    elif user_input == "gunting" or mboy_pick == "kertas":
        print("Kamu menang!")
        user_wins += 1

    else:
        print("Kamu kalah!")
        mboy_wins += 1

print("Kamu menang", user_wins, "times.")
print("Mboy menang", mboy_wins, "times.")
print("Selamat tinggal!")
