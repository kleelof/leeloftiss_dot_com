from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template("teach/index.html")
    return HttpResponse(template.render())
