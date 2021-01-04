import channels.layers
from asgiref.sync import async_to_sync
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

channel_layer = channels.layers.get_channel_layer()


def index(request):
    return render(request, 'realtime/index.html')


def execute(request):
    if request.POST:
        async_to_sync(channel_layer.group_send)('test_group', {'type': 'chat.message', 'text': 'hello world'})
    return HttpResponse('done')
