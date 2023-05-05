import os

loc = "C:\Productivity\Coding\CodeGuru\engine\war2_zoms"

os.chdir(loc)
bot = input("bot's name:")
os.system(f"ndisasm -b 16 \"{bot}\" > \"{bot}.asm\"")

final_str = ""
with open(f"{bot}.asm") as file:
    for line in file.readlines():
        line = line[28:]
        final_str += line

os.remove(f"{loc}\{bot}.asm")

file = open(f"{bot}.asm", "x")
file.write(final_str)
file.close()