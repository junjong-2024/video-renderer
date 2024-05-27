from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, TextClip
from moviepy.config import change_settings
change_settings({"FFMPEG_BINARY":"ffmpeg"})

sample_data = {
    'name': 'test1',
    'description': 'hello',
    'team_count': 2,
    'team_member_count': 3,
    'members': [
        { 'role': 'team_a_1', 'team': 0, 'order': 0, 'filename': 'files/3FYjBDgoOTD3YBqcAAAX.webm'},
        { 'role': 'team_a_2', 'team': 0, 'order': 1, 'filename': 'files/hgbnsDarYCNARv3sAAAR.webm'},
        { 'role': 'team_a_3', 'team': 0, 'order': 2, 'filename': 'files/JrDZsNA2xemhHZGDAAAT.webm'},
        { 'role': 'team_b_1', 'team': 1, 'order': 0, 'filename': 'files/k_44xWIsTZklFMhQAAAV.webm'},
        { 'role': 'team_b_2', 'team': 1, 'order': 1, 'filename': 'files/TMrQ_BQ3Kjh1OXb8AAAP.webm'},
        { 'role': 'team_b_3', 'team': 1, 'order': 2, 'filename': 'files/w0Mg4EEG3RvinpLWAAAL.webm'}
    ],
    'rules': [
    { 'debater': 'team_a_1', 'msg': '팀 A 입안', 'time': 10 },
    { 'debater': 'team_b_1', 'msg': '팀 B 입안', 'time': 10 },
    { 'debater': 'team_a_2', 'msg': '팀 A 교차질의', 'time': 10 },
    { 'debater': 'team_b_2', 'msg': '팀 B 교차질의', 'time': 10 },
    { 'debater': 'team_a_3', 'msg': '팀 A 반박', 'time': 10 },
    { 'debater': 'team_b_3', 'msg': '팀 B 반박', 'time': 10 },
    { 'debater': 'team_a_1', 'msg': '팀 A 마무리', 'time': 10 },
    { 'debater': 'team_b_1', 'msg': '팀 B 마무리', 'time': 10 }
  ]
}

members = {}
clips = []

duration = 0

for rule in sample_data['rules']:
    duration = duration + rule['time']

blank_clip = ColorClip(size=(1920, 1080), color=(0,0,0), duration=duration)

clips.append(blank_clip)

for member in sample_data['members']:
    i = member['team']
    j = member['order']
    video = VideoFileClip(member['filename']).set_position((600 * j, 450 * i))
    members[member['role']] = video

for video in members.values():
    clips.append(video)

timestamp = 0
for rule in sample_data['rules']:
    timestamp = timestamp + rule['time']
    txt = TextClip(rule['msg'], fontsize=50, font='NanumGothic', color='white', bg_color='transparent') \
        .set_position((600, 600))\
        .set_start(timestamp)\
        .set_duration(rule['time'])
    # clips.append(txt)

print(clips)
final_clip = CompositeVideoClip(clips)

final_clip.write_videofile("output_video.mp4",
        threads=12,
        codec="h264_videotoolbox"
    )

# movie_1 = 'files/--pr7THjjbfIX0IgAAAF.webm'
# movie_2 = 'files/o-ZQv5GFC0PB2y81AAAB.webm'
#
# # 빈 화면 클립 생성
# width = 1920
# height = 1080
# blank_clip = ColorClip(size=(width, height), color=(0,0,0), duration=8)
#
# video1 = VideoFileClip(movie_1)
# resized_video1 = video1.resize(newsize=(600, 450)) # 640x360 해상도로 리사이징
# video2 = VideoFileClip(movie_2)
# resized_video2 = video2.resize(newsize=(640, 360)) # 640x360 해상도로 리사이징
#
# positioned_video1 = resized_video1.set_position((10, 10))
# positioned_video2 = resized_video2.set_position((670, 10))
#
# square_clip = ColorClip(size=(660, 380), color=(255, 255, 255))\
#     .set_position((0, 0))\
#     .set_start(2)\
#     .set_duration(4)
#
# square_clip_2 = ColorClip(size=(660, 380), color=(255, 255, 255))\
#     .set_position((660, 0))\
#     .set_start(6)\
#     .set_duration(2)
#
# txt_clip_1 = TextClip("토론을 시작합니다.", fontsize=50, font='NanumGothic', color='white', bg_color='transparent')\
#     .set_position((600, 600))\
#     .set_duration(2)
#
# txt_clip_2 = TextClip("1번 발언 차례입니다.", fontsize=50, font='NanumGothic', color='white', bg_color='transparent')\
#     .set_position((600, 600))\
#     .set_start(2)\
#     .set_duration(4)
#
# txt_clip_3 = TextClip("2번 발언 차례입니다.", fontsize=50, font='NanumGothic', color='white', bg_color='transparent')\
#     .set_position((600, 600))\
#     .set_start(6)\
#     .set_duration(2)
#
# final_clip = CompositeVideoClip([blank_clip,square_clip, square_clip_2, positioned_video1, positioned_video2, txt_clip_1, txt_clip_2, txt_clip_3])
#
# final_clip.write_videofile("output_video.mp4")
