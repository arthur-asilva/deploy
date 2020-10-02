from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os

def UploadArquivos(request):
    
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)

    return render(request, 'index.html', {'data': os.listdir('media')})
