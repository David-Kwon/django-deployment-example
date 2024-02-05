from django.shortcuts import render

# Create your views here.
def index(requests):
    context_dict = {'text':'hello world', 'number':100}
    return render(requests, 'basic_app/index.html',context_dict)

def other(requests):
    return render(requests, 'basic_app/other.html')

def relative(requests):
    return render(requests, 'basic_app/relative_url_templates.html')