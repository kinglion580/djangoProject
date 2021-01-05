import uuid
import time
import subprocess
import channels.layers
from asgiref.sync import async_to_sync
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
channel_layer = channels.layers.get_channel_layer()


def index(request):
    user_uuid = str(uuid.uuid4())
    return render(request, 'realtime/index.html', {'user_uuid': user_uuid})


def execute(request):
    if request.POST:
        run_cmd('python djangoProject/echo.py')
    return HttpResponse('done')


def run_cmd(shell_cmd):
    cmd = shell_cmd.split()
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline().strip()
        if line:
            print(line.decode('utf-8'))
            async_to_sync(channel_layer.group_send)('test_group', {'type': 'chat.message', 'text': line.decode('utf-8')})
    if p.returncode == 0:
        print('subprogram success')
    else:
        print('subprogram failed')