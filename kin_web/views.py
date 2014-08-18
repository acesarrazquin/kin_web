from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def now(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)

def plus(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()

    time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours, it will be %s.</body></html>"%(offset, time)
    return HttpResponse(html)

def meta(request):

    first_fields = {'path':request.path,
                    'host':request.get_host(),
                    'fullpath':request.get_full_path(),
                    'secure':request.is_secure()}.items()

    fields = request.META.items()



    fields.sort()
    print(fields)
    meta_dic = render(request, 'example.html', {'meta_list': fields,
                                                'list1':first_fields})

    return meta_dic

