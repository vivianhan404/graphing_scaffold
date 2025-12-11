import os

folder = 'img/transitions'
for i in range(1, 16):
  os.rename(f"{folder}/{i}.png", f"{folder}/jumbled_{i}.png")
  os.rename(f"{folder}/{i+15}.png", f"{folder}/scaffold_{i}.png")