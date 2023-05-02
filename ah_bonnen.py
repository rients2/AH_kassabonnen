import io
import PyPDF2
from PIL import Image

pdf_path = 'ah_bonnen\\2023-01-03_AH_kassabon.pdf'
pdf_img_path = 'ah_bonnen_img/'

# Open the PDF file
pdf_file = open(pdf_path, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Extract the first page of the PDF file
page = pdf_reader.getPage(0)

# Look for the image object in the '/XObject' dictionary within the '/Resources' dictionary
resources = page['/Resources'].getObject()
xobject = resources['/XObject']

# Get the image data using the key for the image object in the '/XObject' dictionary
image_obj = xobject['/X0'].getObject()
image_data = image_obj.getData()
#print(image_data)