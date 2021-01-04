import uuid
import channels.layers
from asgiref.sync import async_to_sync
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

channel_layer = channels.layers.get_channel_layer()


def index(request):
    user_uuid = str(uuid.uuid4())
    request.session['current_user'] = user_uuid
    print(user_uuid)
    return render(request, 'realtime/index.html')


def execute(request):
    if request.POST:
        user_uuid = request.session['current_user']
        print(user_uuid)
        async_to_sync(channel_layer.group_send)(user_uuid, {'type': 'chat.message', 'text': 'hello world'})
    return HttpResponse('done')
