from rembg import remove
from PIL import Image

input_path='a.jpg'
output_path='a.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
