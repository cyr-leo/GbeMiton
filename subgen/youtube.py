import re
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
import os

from GbéMiton import settings
from .lang import *


def extract_youtube_video_id(url):
    # Pattern pour extraire l'ID de la vidéo YouTube depuis l'URL
    pattern = r"(?<=v=)[a-zA-Z0-9_-]+"

    # Recherche du pattern dans l'URL
    match = re.search(pattern, url)

    if match:
        return match.group()
    else:
        return None


# # Demande à l'utilisateur de saisir l'URL YouTube
# url = input("Veuillez saisir l'URL de la vidéo YouTube : ")

# Extraction de l'ID de la vidéo


def get_video_title(video_url):
    response = requests.get(video_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    meta_title_tag = soup.find('meta', attrs={'name': 'title'})
    if meta_title_tag:
        return meta_title_tag['content']
    else:
        return None


def sub(url):
    videoID = extract_youtube_video_id(url)
    # if videoID:
    #     print("L'ID de la vidéo YouTube est :", videoID)
    if not videoID:
        print("Impossible de trouver l'ID de la vidéo YouTube dans l'URL fournie.")

    # Récupération de la langue des sous-titres
    langue = get_video_language(videoID)

    print("La langue de la vidéo est :", langue)

    meta_title = get_video_title(url)
    print(f"Titre de la page : {meta_title}")

    transcript = YouTubeTranscriptApi.get_transcript(videoID, languages=[langue])

    formatter = SRTFormatter()

    # .format_transcript(transcript) turns the transcript into a TXT string.
    txt_formatted = formatter.format_transcript(transcript)

    documents_dir = os.path.join(settings.BASE_DIR, 'static', 'documents')
    if not os.path.exists(documents_dir):
        os.makedirs(documents_dir)

    file_name = f'{meta_title}.srt'

    file_path = os.path.join(documents_dir, file_name)

    # Now we can write it out to a file.
    with open(file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(txt_formatted)

    capfile = f'{file_path}'
    print('finished')
    print(f'{capfile}')
    return capfile


