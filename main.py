import redis
import render_ffmpeg
import json
import uuid
import os

r = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, decode_responses=True)

while True:
    _, v = r.brpop('render')
    render_ffmpeg.render(json.loads(v), f'{uuid.uuid4().hex}.mp4')