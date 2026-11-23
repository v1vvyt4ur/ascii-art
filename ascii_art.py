import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

img = Image.open("test-imgs/IMG_7334.JPG")
img_array = np.array(Image.open("test-imgs/IMG_7334.JPG"))
img2_array = np.array(Image.open("test-imgs/wtjMp4rL_400x400.jpeg"))
w=img.width
h=img.height

density = "█▓▒░ "
#density = "@%#*+=-:. "
#density="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
print(density)


gray = np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
gray2=np.dot(img2_array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

for i in range(0,w,5):
    for j in range(0,h,5):
        #r, g, b = img_array[i][j]
        if len(density) == 5:
            print(f"{density[gray[i][j]//51]}{density[gray[i][j]//51]}", end="")
        elif len(density) == 10:
            print(f"{density[gray[i][j]//28]} ", end="")
        else:
            print(f"{density[gray[i][j]//4]} ", end="")
    print()

for i in range(0,w,5):
    for j in range(0,h,5):
        if len(density) == 5:
            print(f"{density[gray2[i][j]//51]}{density[gray2[i][j]//51]}", end="")
        elif len(density) == 10:
            print(f"{density[gray2[i][j]//28]} ", end="")
        else:
            print(f"{density[gray2[i][j]//4]} ", end="")
    print()

print(img.format, img.size, img.mode)