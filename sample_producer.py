import time
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

for i in range(10):
    print(i)
    r.lpush('render', f'hello {i}')
    time.sleep(1)


sample_data = {
    'name': 'test1',
    'description': 'hello',
    'team_count': 2,
    'team_member_count': 3,
    'members': [
        { 'role': 'A팀 제1토론자', 'team': 0, 'order': 0},
        { 'role': 'A팀 제2토론자', 'team': 0, 'order': 1},
        { 'role': 'A팀 제3토론자', 'team': 0, 'order': 2},
        { 'role': 'B팀 제1토론자', 'team': 1, 'order': 0},
        { 'role': 'B팀 제2토론자', 'team': 1, 'order': 1},
        { 'role': 'B팀 제3토론자', 'team': 1, 'order': 2}
    ],
    'rules': [

    ]
}