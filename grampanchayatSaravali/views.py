from django.shortcuts import render


def welcome(request):
    from django.core.management import call_command
    call_command("migrate", interactive=False)
    request.session['lang'] = 'en'
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/index.html', {"language": language})

    return render(request, 'grampanchayatSaravali/index.html', {"language": language})


def home(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/index.html', {"language": language})

    return render(request, 'grampanchayatSaravali/index.html', {"language": language})

def workers(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/workers.html', {"language": language})

    return render(request, 'grampanchayatSaravali/workers.html', {"language": language})


def certificates(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/certificates.html', {"language": language})

    return render(request, 'grampanchayatSaravali/certificates.html', {"language": language})


def map(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/maps.html', {"language": language})

    return render(request, 'grampanchayatSaravali/maps.html', {"language": language})



def electedMember(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/electedMember.html', {"language": language})

    return render(request, 'grampanchayatSaravali/electedMember.html', {"language": language})


def photoGallery(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/gallery.html', {"language": language})

    return render(request, 'grampanchayatSaravali/gallery.html', {"language": language})


def faq(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/contact.html', {"language": language})

    return render(request, 'grampanchayatSaravali/contact.html', {"language": language})


def developmentPlan(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/vikasArakhada.html', {"language": language})

    return render(request, 'grampanchayatSaravali/vikasArakhada.html', {"language": language})


def committees(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/committees.html', {"language": language})

    return render(request, 'grampanchayatSaravali/committees.html', {"language": language})


def scm1(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/scm1.html', {"language": language})

    return render(request, 'grampanchayatSaravali/scm1.html', {"language": language})


def scm2(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/scm2.html', {"language": language})

    return render(request, 'grampanchayatSaravali/scm2.html', {"language": language})


def scm3(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/scm3.html', {"language": language})

    return render(request, 'grampanchayatSaravali/scm3.html', {"language": language})


def scm4(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/scm4.html', {"language": language})

    return render(request, 'grampanchayatSaravali/scm4.html', {"language": language})


def scm5(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/scm5.html', {"language": language})

    return render(request, 'grampanchayatSaravali/scm5.html', {"language": language})


def scm6(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/scm6.html', {"language": language})

    return render(request, 'grampanchayatSaravali/scm6.html', {"language": language})


def about(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/about.html', {"language": language})

    return render(request, 'grampanchayatSaravali/about.html', {"language": language})


def other1(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/other1.html', {"language": language})

    return render(request, 'grampanchayatSaravali/other1.html', {"language": language})


def other2(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/other2.html', {"language": language})

    return render(request, 'grampanchayatSaravali/other2.html', {"language": language})

def other3(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/other3.html', {"language": language})

    return render(request, 'grampanchayatSaravali/other3.html', {"language": language})

def other4(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/other4.html', {"language": language})

    return render(request, 'grampanchayatSaravali/other4.html', {"language": language})

def other5(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/other5.html', {"language": language})

    return render(request, 'grampanchayatSaravali/other5.html', {"language": language})

def other6(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/other6.html', {"language": language})

    return render(request, 'grampanchayatSaravali/other6.html', {"language": language})


def other7(request):
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'grampanchayatSaravali/other7.html', {"language": language})

    return render(request, 'grampanchayatSaravali/other7.html', {"language": language})
