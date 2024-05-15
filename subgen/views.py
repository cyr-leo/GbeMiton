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


def upload(request):

    if request.method == 'POST':
        video = vid.objects.create(name="Bawo ni lati ṣagbe 2ha pẹlu 2L ti eya?", cap_fil="subtitles/Yotuba_Comment_labourer_2ha_avec_2L_dessences.vtt", image="images/Screenshot_from_2024-05-15_14-43-49.png", description="lilo ẹrọ ogbin fun itulẹ ati ogbin oke, ṣe alaye awọn ipele ti igbaradi, ibẹrẹ ati iṣẹ ẹrọ naa. Olukọni n ṣe afihan bi o ṣe le lo ẹrọ naa lati mu ilọsiwaju ṣiṣẹ ati didara iṣẹ-ogbin", url="videos/Comment_labourer_2ha_avec_2L_dessences__001.mp4")
        return redirect('subgen:home')
    return render(request, "subgen/upload.html")