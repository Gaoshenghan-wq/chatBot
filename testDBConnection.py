

import redis

r = redis.Redis(
    host='redis-18794.c44.us-east-1-2.ec2.redns.redis-cloud.com',
    port=18794,
    decode_responses=True,
    username="default",
    password="8nViRuqdrhrWc5croORDmLorWqYAsmR9",
)

print(r.ping())