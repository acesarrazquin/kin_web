from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import ContactForm
from django.core.mail import EmailMessage


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