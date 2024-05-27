ffmpeg -i files/3FYjBDgoOTD3YBqcAAAX.webm\
 -i files/hgbnsDarYCNARv3sAAAR.webm\
 -i files/JrDZsNA2xemhHZGDAAAT.webm\
 -i files/k_44xWIsTZklFMhQAAAV.webm\
 -i files/TMrQ_BQ3Kjh1OXb8AAAP.webm\
 -i files/w0Mg4EEG3RvinpLWAAAL.webm\
 -filter_complex\
 "[0:v] setpts=PTS-STARTPTS [a];\
[1:v] setpts=PTS-STARTPTS [b];\
[2:v] setpts=PTS-STARTPTS [c];\
[3:v] setpts=PTS-STARTPTS [d];\
[4:v] setpts=PTS-STARTPTS [e];\
[5:v] setpts=PTS-STARTPTS [f];\
[a][b][c] hstack=inputs=3 [top]; \
[d][e][f] hstack=inputs=3 [bottom]; \
[top]pad=iw:ih+60:0:0:color=black[topmargin]; \
[bottom]pad=iw:ih+60:0:60:color=black[bottommargin]; \
[topmargin][bottommargin] vstack=inputs=2, fps=30,
drawtext=text='테스트':x=(w-text_w)/2:y=(h-text_h)/2:font='NanumGothic':fontsize=36:fontcolor=white:enable='between(t,0,5)'
 "\
 output.mp4
