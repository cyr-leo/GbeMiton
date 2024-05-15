from googleapiclient.discovery import build

# Remplacez 'YOUR_API_KEY' par votre propre clé API YouTube Data

youtube = build('youtube', 'v3', developerKey='AIzaSyAOXe7xjI93G6MeatXrmdk5iVWbAH2f3oc')

def get_video_language(video_id):
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        video_snippet = response['items'][0]['snippet']
        return video_snippet.get('defaultAudioLanguage', 'Unknown')
    else:
        return 'Video not found'

# Exemple d'utilisation avec l'ID d'une vidéo
video_id = 'RsplYfp8f7Q'
language = get_video_language(video_id)

