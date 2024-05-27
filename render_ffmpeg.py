import subprocess


def render(input, filename):
    # members = {}
    videos = []

    video_filter = """[0:v] setpts=PTS-STARTPTS [a];
    [1:v] setpts=PTS-STARTPTS [b];
    [2:v] setpts=PTS-STARTPTS [c];
    [3:v] setpts=PTS-STARTPTS [d];
    [4:v] setpts=PTS-STARTPTS [e];
    [5:v] setpts=PTS-STARTPTS [f];
    [a][b][c] hstack=inputs=3 [top];
    [d][e][f] hstack=inputs=3 [bottom];
    [top]pad=iw:ih+60:0:0:color=black[topmargin];
    [bottom]pad=iw:ih+60:0:60:color=black[bottommargin];
    [topmargin][bottommargin] vstack=inputs=2, fps=30"""

    for member in input['members']:
        videos.append('-i')
        videos.append(member['filename'])

    timestamp = 0
    for rule in input['rules']:
        cur_timestamp = timestamp + rule['time']
        video_filter = video_filter + f",drawtext=text='{rule['msg']}':x=(w-text_w)/2:y=(h-text_h)/2:font='NanumGothic':fontsize=36:fontcolor=white:enable='between(t,{timestamp},{cur_timestamp})'"
        timestamp = cur_timestamp

    video_filter = video_filter + ", drawtext=text='%{pts\:gmtime\:0\:%M\\\\\:%S}':x=1700:y=(h-text_h)/2:font='NanumGothic':fontsize=32:fontcolor=white"

    command = ['ffmpeg'] + videos + ['-filter_complex', video_filter, filename]

    subprocess.run(command)


if __name__ == '__main__':
    sample_data = {
        'name': 'test1',
        'description': 'hello',
        'team_size': 2,
        'team_member_size': 3,
        'members': [
            {'role': 'team_0_0', 'team': 0, 'order': 0, 'filename': 'files/OZu3ow4sJj-XxJPgAAAR.webm'},
            {'role': 'team_0_1', 'team': 0, 'order': 1, 'filename': 'files/Tx6vdTJYldzN41ENAAAT.webm'},
            {'role': 'team_0_2', 'team': 0, 'order': 2, 'filename': 'files/w-bmQf5_d8H99-R9AAAV.webm'},
            {'role': 'team_1_0', 'team': 1, 'order': 0, 'filename': 'files/wq7bOQMB4dfOScYSAAAX.webm'},
            {'role': 'team_1_2', 'team': 1, 'order': 1, 'filename': 'files/XQ1i3hLD44CVyegeAAAP.webm'},
            {'role': 'team_1_3', 'team': 1, 'order': 2, 'filename': 'files/Zdfmr-iNqcX_4vJLAAAN.webm'}
        ],
        'rules': [
            {'debater': 'team_a_1', 'msg': '팀 A 입안', 'time': 5},
            {'debater': 'team_b_1', 'msg': '팀 B 입안', 'time': 5},
            {'debater': 'team_a_2', 'msg': '팀 A 교차질의', 'time': 5},
            {'debater': 'team_b_2', 'msg': '팀 B 교차질의', 'time': 5},
            {'debater': 'team_a_3', 'msg': '팀 A 반박', 'time': 5},
            {'debater': 'team_b_3', 'msg': '팀 B 반박', 'time': 5},
            {'debater': 'team_a_1', 'msg': '팀 A 마무리', 'time': 5},
            {'debater': 'team_b_1', 'msg': '팀 B 마무리', 'time': 5}
        ]
    }
    render(sample_data, 'output.mp4')
