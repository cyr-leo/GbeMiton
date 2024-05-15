import re
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter


def extract_youtube_video_id(url):
    # Pattern pour extraire l'ID de la vidéo YouTube depuis l'URL
    pattern = r"(?<=v=)[a-zA-Z0-9_-]+"

    # Recherche du pattern dans l'URL
    match = re.search(pattern, url)

    if match:
        return match.group()
    else:
        return None




def get_video_title(video_url):
    response = requests.get(video_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    meta_title_tag = soup.find('meta', attrs={'name': 'title'})
    if meta_title_tag:
        return meta_title_tag['content']
    else:
        return None




def donw_str_sub(videoID):

    transcript = YouTubeTranscriptApi.get_transcript(videoID, languages=[langue])

    formatter = SRTFormatter()

    # .format_transcript(transcript) turns the transcript into a TXT string.
    txt_formatted = formatter.format_transcript(transcript)

    return txt_formatted


def save_file(txt_formatted, meta_title ):
    # Now we can write it out to a file.
    with open(f'{meta_title}.srt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(txt_formatted)





def subdown(url):
    # Demande à l'utilisateur de saisir l'URL YouTube
    # url = input("Veuillez saisir l'URL de la vidéo YouTube : ")
    print('start')
    url = url

    # Extraction de l'ID de la vidéo
    videoID = extract_youtube_video_id(url)

    # if videoID:
    #     print("L'ID de la vidéo YouTube est :", videoID)
    # else:
    #     print("Impossible de trouver l'ID de la vidéo YouTube dans l'URL fournie.")

    # Récupération de la langue des sous-titres
    # langue = input("Veuillez saisir la langue des sous-titres YouTube : fr, en, es, de ?")

    langue = 'fr'

    meta_title = get_video_title(url)

    txt_formatted = donw_str_sub(videoID)

    save_file(txt_formatted, meta_title)


