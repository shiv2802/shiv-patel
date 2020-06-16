from PIL import Image
import os

filename = "imgtopdf.gif"
im = Image.open(filename)
if im.mode == "RGBA":
    im = im.convert("RGB")
new_file = "imgtopdf.pdf"
if not os.path.exists(new_file):
    im.save(new_file, "PDF", resolution=1000.0)
print("done")