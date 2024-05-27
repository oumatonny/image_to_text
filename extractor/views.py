from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image
import pytesseract

def upload_image(request):
    extracted_text = ""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_upload = form.save()
            image_path = image_upload.image.path
            image = Image.open(image_path)
            extracted_text = pytesseract.image_to_string(image)
    else:
        form = ImageUploadForm()
    
    return render(request, 'extractor/upload_image.html', {'form': form, 'extracted_text': extracted_text})
