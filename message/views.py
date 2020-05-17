from django.http.response import JsonResponse
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.csrf import csrf_exempt
import json

from message.models import Message


@csrf_exempt
def board(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['nickname']
        message = data['message']
        print(username, message)
        if username and message:
            Message.objects.create(username=username, message=message)
            return JsonResponse({'msg': '留言成功', 'code': 200})
        return JsonResponse({'msg': '留言或昵称不能为空'})


def formatTime(message):
    message['addtime'] = message['addtime'].strftime('%Y-%m-%d %H:%M:%S')
    return message


@csrf_exempt
def selectAll(request):
    page = request.GET.get('page')
    pagesize = request.GET.get('pagesize')
    queryset = Message.objects.all().order_by('-addtime')
    paginator = Paginator(queryset, pagesize)
    try:
        paginator_result = paginator.page(number=page)
        result = list(map(formatTime, [i for i in paginator_result.object_list.values()]))
        data = {
            'msg': 'success',
            'code': 200,
            'total': queryset.count(),
            'data': result
        }
        return JsonResponse({'data': data})
    except EmptyPage:
        return JsonResponse({'msg': 'success', 'data': []})

