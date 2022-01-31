"""
Celery 실행 방법:
celery -A tasks worker --loglevel=INFO --concurrency=3 -n worker1@%h
"""
import os
import redis
from celery import Celery
from dotenv import load_dotenv

load_dotenv(override=True)

IS_DOCKER = bool(int(os.getenv('DOCKER', 0)))

RABBIT_HOST = os.getenv('RABBIT_HOST')
RABBIT_USER = os.getenv('RABBIT_USER')
RABBIT_PASS = os.getenv('RABBIT_PASS')
RABBIT_PORT = os.getenv('RABBIT_PORT')

if IS_DOCKER and RABBIT_HOST == 'localhost':
    REMOTE_RABBIT_HOST = 'host.docker.internal'

RABBIT_URL = f'amqp://{RABBIT_USER}:{RABBIT_PASS}@{RABBIT_HOST}:{RABBIT_PORT}/'

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PASS = os.getenv('REDIS_PW')
REDIS_PORT = os.getenv('REDIS_PORT')

if IS_DOCKER and REDIS_HOST == 'localhost':
    REDIS_HOST = 'host.docker.internal'

REDIS_URL = f'redis://:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}/0'

app = Celery('tasks', broker=RABBIT_URL, backend=REDIS_URL, result_expires=(60 * 60 * 4))
cache = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASS)

app.conf.celery_timezone = 'Asia/Seoul'
app.conf.celery_enable_utc = True
