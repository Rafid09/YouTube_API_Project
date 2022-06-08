from googleapiclient.discovery import build

youTubeApiKey = "AIzaSyAa0lcHl5NyInUcTbU4EDxTS2nZk7kjhM0"
youtube = build('youtube', 'v3', developerKey=youTubeApiKey)
channelId = 'UCHDFNoOk8WOXtHo8DIc8efQ'

statdata = youtube.channels().list(part='statistics', id=channelId).execute()
print(statdata)

stats = statdata['items'][0]['statistics']
print("Stats are given below:")
print(stats)

videoCount = stats['videoCount']
print("Total Number of Videos:")
print(videoCount)

viewCount = stats['viewCount']
print("Total Watch Time:")
print(viewCount)

subscriberCount = stats['subscriberCount']
print("Total Number of Subscribers:")
print(subscriberCount)

snippetdata = youtube.channels().list(part='snippet', id=channelId).execute()
print(snippetdata)

title = snippetdata['items'][0]['snippet']['title']
print("Title of YouTube channel:")
print(title)

description = snippetdata['items'][0]['snippet']['description']
print("YouTube Channel’s Description:")
print(description)

logo = snippetdata['items'][0]['snippet']['thumbnails']['default']['url']
print("YouTube Channel’s Logo:")
print(logo)

print("Getting Content Details:")

print("Getting All the Video Details:")

contentdata = youtube.channels().list(id=channelId, part='contentDetails').execute()
playlist_id = contentdata['items'][0]['contentDetails']['relatedPlaylists']['uploads']
videos = []

next_page_token = None

while 1:
    res = youtube.playlistItems().list(playlistId=playlist_id,
                                       part='snippet',
                                       maxResults=50,
                                       pageToken=next_page_token).execute()
    videos += res['items']
    next_page_token = res.get('nextPageToken')

    if next_page_token is None:
        break

print(videos)

video_ids = list(map(lambda x: x['snippet']['resourceId']['videoId'], videos))
print("Getting Video ID for each Video:")
print(video_ids)

'''
stats = [] for i in range(0, len(video_ids), 40):
res = (youtube).videos().list(id=','.join(video_ids[i:i+40]),part='statistics').execute()
stats += res['items']
print(stats)
'''

print("Collecting All the Information in a List:")
title = []
liked = []
disliked = []
views = []
url = []
comment = []

for i in range(len(videos)):
    title.append((videos[i])['snippet']['title'])
    url.append("https://www.youtube.com/watch?v=" + (all_videos[i])['snippet']['resourceId']['videoId'])  # unresolved issue
    liked.append(int((stats[i])['statistics']['likeCount']))
    disliked.append(int((stats[i])['statistics']['dislikeCount']))
    views.append(int((stats[i])['statistics']['viewCount']))
    comment.append(int((stats[i])['statistics']['commentCount']))
