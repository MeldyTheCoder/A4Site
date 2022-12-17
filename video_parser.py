import json
import os

import config
from pyyoutube import Api

class VideoParser:
    def __init__(self):
        self.video_post_url = 'https://www.googleapis.com/youtube/v3/search?key={key}&channelId={channel_id}&part=snippet,id&order=date&maxResults={max_results}'
        self.channel = config.channel_id
        self.api = Api(api_key=config.youtube_api_key)
        self.max_results = 10
        self.video_url_pattern = 'https://youtube.com/watch?v={video_id}'

    def __convert_list(self, list_data: list, single: bool = False):
        if not single:
            new_data = [{"video_url" : self.video_url_pattern.format(video_id=data['id']['videoId']),
                         "title" : data['snippet']['title'], 'image' : data['snippet']['thumbnails']['medium']['url'],
                         'video_id' : data['id']['videoId']} for data in list_data]

        else:
            new_data = [{"video_url" : self.video_url_pattern.format(video_id=data['id']),
                         "title" : data['snippet']['title'], 'image' : data['snippet']['thumbnails']['medium']['url'],
                         'video_id' : data['id'], 'views' : data['statistics']['viewCount'],
                         'likes' : data['statistics']['likeCount']} for data in list_data][0]
        return new_data

    def get_videos(self):
        data = self.api.session.get(self.video_post_url.format(key=config.youtube_api_key, channel_id=self.channel, max_results=10))
        data = json.loads(data.text)
        if not data:
            return []
        video_list = data['items']
        video_list = self.__convert_list(video_list)
        return video_list

    def get_video(self, video_id: str):
        data = self.api.get_video_by_id(video_id=video_id, return_json=True)
        data = self.__convert_list(data['items'], True)
        return data

    def get_channel_info(self):
        data = self.api.get_channel_info(channel_id=self.channel, return_json=True)
        return data

