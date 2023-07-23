
from cmath import rect
from PIL import Image, ImageDraw
from tqdm import trange

#Settings============
sizeTheCanvasX = 2560
sizeTheCanvasY = 1440
Nums           = 1000
Zoom           = 0.5
#Settings============

PriNums = [2,3]
i = 2

imgbg = Image.new("1", (sizeTheCanvasX, sizeTheCanvasY), 0)
img = ImageDraw.Draw(imgbg)

for i in trange(2,Nums):
    i += 1
    isPrime = True
    for CurNum in PriNums[:-1]:
        if i % CurNum == 0:         #Is Not Prime
            isPrime = False
            break
    if isPrime == True: PriNums.append(i)

#print(PriNums)

j = 0
for i in PriNums:
    Pos = rect(i, i)
    img.point((Pos.real*Zoom+sizeTheCanvasX/2, Pos.imag*Zoom+sizeTheCanvasY/2),fill=1)
imgbg.show()
