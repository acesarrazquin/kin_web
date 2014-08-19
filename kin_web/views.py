from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from forms import ContactForm
from django.core.mail import send_mail

def main(request):
    return render(request, "main_menu.html")

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

def search_form(request):
    return render(request, "search_form.html")

def search(request):
    if request.GET['q']=='':
        message = "You submitted an empty form."
    else:
        message = "You searched for: %s"%request.GET['q']

    return HttpResponse(message)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['noreply@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject':"I love your site!"}
        )

    return render(request, 'contact_form.html', {'form': form})

def thanks(request):
    return HttpResponse("<h1>Tnaks!</h1>")