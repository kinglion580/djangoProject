import os
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.conf import settings
from .forms import FilesForm

# Create your views here.

media_path = os.path.join(settings.BASE_DIR, 'files')


class IndexView(View):
    def get(self, request):
        files_form = FilesForm(request.POST, request.FILES)
        return render(request, 'home.html', {'files_form': files_form})

    def post(self, request):
        files_form = FilesForm(request.POST, request.FILES)
        if files_form.is_valid():
            files = request.FILES.getlist('files')
            for file in files:
                handle_uploaded_file(file, media_path)
            return JsonResponse({'message', 'xxx'})


def handle_uploaded_file(file, dst_path):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    with open(os.path.join(dst_path, file.name), 'wb+') as dst:
        for chunk in file.chunks():
            dst.write(chunk)
