import redis
import os
import uuid
import queue
import subprocess
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379)
client = redis.Redis(connection_pool=redisPool)


def index(request):
    user_uuid = str(uuid.uuid4())

    #q.put('hello world')
    #q.put('second string')

    return render(request, 'redis_queue/index.html', {'user_uuid': user_uuid})


def execute(request):
    if request.POST:
        user_uuid = request.POST.get('user_uuid')
        run_cmd('python djangoProject/echo.py', user_uuid)
        client.lpush(user_uuid, 'done')
    return JsonResponse({'queue_dict': 'xxx'})


def get_message(request, user_uuid):
    #print(user_uuid)
    message = client.brpop(user_uuid)[1]
    if message == 'done':
        # client.delete(user_uuid)
        pass
    return HttpResponse(message)


def run_cmd(shell_cmd, q_name):
    cmd = shell_cmd.split()
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline().strip()
        if line:
            print(line.decode('utf-8'))
            client.lpush(q_name, line.decode('utf-8'))
    if p.returncode == 0:
        print('subprogram success')
    else:
        print('subprogram failed')
