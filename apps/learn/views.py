from django.shortcuts import render
from django.http import HttpResponse
from .models import Chapter, Level
from django.views import View
from .utils import tach_4socuoi
# Create your views here.


# def index(request):
#     cterls = Chapter.objects.all()
#     print(cterls)
#
#     return render(request, "index.html", {'var1': cterls, 'isprint': False})


class IndexView(View):

    def get(self, request):
        #cterls = Chapter.objects.all()
        # cterls = Chapter.objects.filter(id__gt=3)
        # lv = Level.objects.get(id=2)
        cterls = Chapter.objects.filter(level_id=1)
        return render(request, "index.html", {'var1': cterls, 'isprint': False})

    def post(self, request):
        data = request.POST['username']
        Level.objects.create(name=data)
        result = tach_4socuoi(phonenumer=data)

        return HttpResponse("themn thanh cong va tach thanh cong la: "+ result)


class LichHoc(View):
    def get(self, request):
        cterls = Chapter.objects.filter(level_id=1)
        context = {
            'chapters':  cterls
        }
        return render(request, 'table.html', context)

    def post(self):
        pass

    def delete(self):
        pass
