import os
from PIL import Image

imageDir = ""
saveDir  = ""

for file in os.listdir(imageDir):
    count = 1
    while count <= 36:
        img = Image.open(os.path.join(imageDir, file))
        saveName= file[:-4]+str(count)+".png"
        img = img.rotate(count*10,expand=True)
        img.save(os.path.join(saveDir, saveName))
        count += 1
