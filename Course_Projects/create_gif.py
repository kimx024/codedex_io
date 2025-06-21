"""
This script allows the user to create a Graphics Interchange Format (GIF), with the help of the module imagio
The pictures labeled team_pic 1 and team_pic2 sourced are from the beginners course on Codédex.
The picture eyes_open and eyes_closed are generate by ChatGPT model 4o.

This script is part of my (@milakim) Codédex final project called "Create a Gif in Python" of the
beginner Python course. A successful completion will result in the certificate for a beginner level of Python
"""

###### First part: a  GIF of the team of behind Codéx
import imageio.v3 as iio

filenames = ['team_pic1.png', 'team_pic2.png']
images = []

# Read and append the files stored in the variables to a new list
for filename in filenames:
  images.append(iio.imread(filename))

# Make magic with the imageio module and write a gif, which takes the duration in ms (how long each picture is show)
# and the amount of repetition (loop) with 0 meaning it will loop forever
iio.imwrite('team.gif', images, duration=500, loop=0)

###### Second part - make your own: a blinking robot
my_filenames = ['eyes_open.png', 'eyes_closed.png']
my_images = []

for filename in my_filenames:
  my_images.append(iio.imread(filename))

iio.imwrite('blinking_eyes.gif', my_images, duration=500, loop=0)