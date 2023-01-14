from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *

# defining function
def indexm(request):
    # checking whether request.method is post or not
    movies=File.objects.all()
    if request.method == 'POST':
        return render(request, 'index.html')
    context={'movies':movies}
    return render(request, 'index.html',context)

def indexs(request):
    # checking whether request.method is post or not
    categorie=Type.objects.all()
    movies=Series.objects.all()
    if series:
        movies=Series.objects.filter(seriename = series).order_by('?')
        context={'categorie' :categorie,'types':types,'movies':movies}
        return render(request, 'index.html',context)
    if types:
        series=Series.objects.filter(types = types).order_by('?')
        movies=File.objects.filter(types = types).order_by('?')
        context={' types':types,'movies':movies,'categorie' :categorie}
        return render(request, 'index.html',context)
    context={'categorie' :categorie,' types':types,'movies':movies}
    return render(request, 'index.html',context)


def download(request, path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404
