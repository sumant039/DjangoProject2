# created this file by MYSELF


from django.http  import HttpResponse
from django.shortcuts import render


#def index(request):
 #   return  HttpResponse('''<h1>hello sumant</h1>  <a href="https://stackoverflow.com/questions/24682155/django-user-registration-with-error-no-such-table-auth-user">Click Here</a>''')
def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    punctuations = '''!()-[];:'\,<>./?@#$%^&*'''
    #analyzed=djtext
    analyzed=""
    for char in djtext:
        if char not in  punctuations:
            analyzed=analyzed + char
    params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
    return render(request,'analyze.html',params)