import redis
import render_ffmpeg
import json
import os

r = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, decode_responses=True)


def print_log(*args):
    print(' '.join([str(arg) for arg in args]), end="\n")


while True:
    _, v = r.brpop('render')
    data = json.loads(v)
    print_log(data)
    render_ffmpeg.render(data)