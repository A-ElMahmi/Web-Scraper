import os

subDirectories = [f for f in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), f)) and not f.startswith(".")]

for i, j in enumerate(subDirectories):
  print(f"{i} {j}")

index = int(input("Choose a program to run: "))
print()

os.system(f"python {subDirectories[index]}/main.py")