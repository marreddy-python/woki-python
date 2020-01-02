import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = 'AIzaSyCrHUcVKB4EGphftwg_Xr1RhfqyqlP2h70'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
    
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q = options['q'],
    part='id,snippet',
    maxResults=options['max_results']
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):

    if search_result['id']['kind'] == 'youtube#video':
      videos.append(search_result['id']['videoId'])


  print('Videos:\n', '\n'.join(videos), '\n')
  
  return videos

 

 