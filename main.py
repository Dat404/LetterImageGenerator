from PIL import Image, ImageFont, ImageDraw
from random import choice, randint


print('''Made by Daxya(DAT404, RennDie)
for start write image size...''')

w,h = map(int, input('Image size(width [space] height) /> ').split())
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ%!$[]<>&123456789 '
FontSize = 40
x = 0 
y = -5

GeneratedImage = Image.new(mode = 'RGB', size = (w, h))
ImageFont_ = ImageFont.truetype('fonts\\better-vcr_0.ttf', FontSize)
FinalImage = ImageDraw.Draw(GeneratedImage)

for i in range(0, w+h):
	FinalImage.text((x, y), choice(symbols), (randint(0, 255), randint(0, 255), randint(0, 255)), font = ImageFont_)
	y += 40
	if y >= h:
		print(x,y)
		y = 0
		x += 40
		if x >= w:
			break

GeneratedImage.show()
