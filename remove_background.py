from rembg import remove
import easygui
from PIL import Image

inputpath = easygui.fileopenbox(title='Select image file')
outpath = easygui.filesavebox(title='Save the file too..')

input_image = Image.open(inputpath)
output_image = remove(input_image)


output_image = output_image.convert('RGB')
output_image.save(outpath)
