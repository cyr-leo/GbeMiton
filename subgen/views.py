from django.conf.urls.static import static
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from subgen.forms import SubgenForm
from subgen.subdowloader import subdown
from .models import vid
from .youtube import sub
from .trans2 import trans


@method_decorator(csrf_exempt, name='dispatch')
def index(request):
    if request.method == 'POST':
        form = SubgenForm(request.POST)
        if form.is_valid():
            subdown(request.POST.get("url"))
    else:
        request.GET.get('url')

    return render(request, "subgen/index.html")


def home(request):
    vids = vid.objects.all()

    return render(request, "subgen/index.html", {"vids": vids})


def video(request, v_id):
    vide = vid.objects.get(pk=v_id)

    return render(request, "subgen/video.html", {"vid": vide})

def generate(request):
    url = request.GET.get("url")
    if url:
        src_file = sub(url)
        trans(src_file)

        file_path = '/static/documents/votre_fichier.json'

        file_url = static(file_path)

        return JsonResponse({'results': request.build_absolute_uri(file_url)})

    return HttpResponse("Evenement non trouvé !!! ")
# Create your views here.
