# youtube.py

from googleapiclient.discovery import build
from pathlib import Path

def youtube_channel_detail(channel_id, api_key):
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    search_response = youtube.channels().list(part='snippet,statistics',id=channel_id,).execute()
    return search_response['items'][0]

def main():
    channel_id = "" 
    api_key = ""
    date = youtube_channel_detail('channel_id', 'api_key') 
    path = Path.cwd() / Path(__file__).parents[0] / "speak.txt"
    file = open(path, 'w',encoding='UTF-8')
    file.write('{channel}チャンネルの登録者数は{subscribe}人です'.format(channel=date['snippet']['title'],subscribe=date['statistics']['subscriberCount']))
    file.close()

if __name__ == '__main__':
    main()