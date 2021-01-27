from django.shortcuts import render
from django.http import HttpResponse
from .models import Chapter, Level
from django.views import View
# Create your views here.


# def index(request):
#     cterls = Chapter.objects.all()
#     print(cterls)
#
#     return render(request, "index.html", {'var1': cterls, 'isprint': False})


class IndexView(View):

    def get(self, request):
        cterls = Chapter.objects.all()
        return render(request, "index.html", {'var1': cterls, 'isprint': False})

    def post(self, request):
        data = request.POST['username']
        Level.objects.create(name=data)

        return HttpResponse("themn thanh cong")