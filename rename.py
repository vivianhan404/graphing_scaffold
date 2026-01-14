import os

folder = 'img/t'
for i in range(1, 17):
  os.rename(f"{folder}/{i}.png", f"{folder}/jumbled_{i}.png")
  os.rename(f"{folder}/{i+16}.png", f"{folder}/scaffold_{i}.png")