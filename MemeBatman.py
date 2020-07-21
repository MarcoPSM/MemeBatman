from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


original_img = "/home/marco/Pictures/batman.png"
output_img = "meme-batman.png"

robin_text = "Vai estudar o \n past simple"
batman_text = "Isso já passou"

black = (0, 0, 0)

img = Image.open(original_img)
draw = ImageDraw.Draw(img)

robin_font = ImageFont.truetype("DejaVuSerif.ttf", 24)
batman_font = ImageFont.truetype("DejaVuSerif-Bold.ttf", 24)

draw.text((30, 20), robin_text, black, font=robin_font)
draw.text((270, 30), batman_text, black, font=batman_font)

img.save(output_img)
