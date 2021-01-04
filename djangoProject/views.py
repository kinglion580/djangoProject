import os
import uuid
import queue
import subprocess
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

q = queue.Queue()


def index(request):
    #
    #q.put('hello world')
    #q.put('second string')

    return render(request, 'index.html', {'queue_dict': 'xxx'})


def execute(request):
    if request.POST:
        q.put('checking....')
        run_cmd('python djangoProject/echo.py', q)
        #run_cmd('netstat', q)
        #os.chdir('Z:/jdm/204-568-603')
        #run_cmd('step_out 204-568-603.brd -o 204-568-603 -n -d -i -v', q)
        q.put('output1...')
        q.put('output2...')
        q.put('output3...')
        q.put('done')

    return JsonResponse({'queue_dict': 'xxx'})


def get_message(request):
    message = q.get()
    return HttpResponse(message)


def run_cmd(shell_cmd, q):
    cmd = shell_cmd.split()
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline().strip()
        if line:
            print(line.decode('utf-8'))
            q.put(line.decode('utf-8'))
    if p.returncode == 0:
        print('subprogram success')
    else:
        print('subprogram failed')
