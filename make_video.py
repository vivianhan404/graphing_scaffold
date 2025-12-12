import moviepy
import os

def convert2(filename):
  # shortcut
  convert(filename, filename, filename)

def convert(img, mp3, mp4):
  print(img, mp3, mp4)
  image = moviepy.ImageClip(f"img/{img}.png")

  audio = moviepy.AudioFileClip(f"mp3/{mp3}.mp3")

  video = moviepy.CompositeVideoClip([image.with_duration(audio.duration)])
  video = video.with_audio(audio)

  video.write_videofile(f"mp4/{mp4}.mp4", fps=30)

# for filename in os.listdir('img'):
#   name = filename[:-4]
#   if name == '.DS_S' or name + ".mp4" in os.listdir('mp4'):
#     continue
#   print(name)
#   convert(name)
# diff = {
#   6: '4_alien_intro',
#   7: '8_ice_cream_intro',
#   9: '5_alien2_intro',
#   12: '6_fruits_intro',
#   14: '7_toy_intro'
# }
for i in range(1, 16):
  convert('transitions/jumbled_' + str(i), 'transition', 'transition_jumbled_' + str(i))
# convert('18', 'done', 'done')