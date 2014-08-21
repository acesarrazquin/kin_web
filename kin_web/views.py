from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from forms import ContactForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def main(request):
    return render(request, "base.html")

def examples(request):
    return render(request, "cssportal.html")

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


def home(request):
    return render(request, 'home.html', {'home':'active'})

def downloads(request):
    return render(request, 'downloads.html', {'downloads':'active'})

def about(request):
    return render(request, 'about.html', {'about':'active'})

def thanks(request):
    email = request.session.get('email', False)
    return render(request, 'thanks.html', {'email': email,
                                           'contact': 'active'})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd.get('email','')
            em = EmailMessage(
                cd['subject'],
                cd['message'],
                'noreply@noreply.com', # change this name
                to = ['acesarrazquin@cemm.oeaw.ac.at'],
            )
            em.send()
            request.session['email'] = email
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject':""}
        )
    return render(request, 'contact.html', {'form': form,
                                            'contact':'active'})