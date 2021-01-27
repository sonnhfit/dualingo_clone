from django.urls import path
from .views import IndexView, LichHoc

urlpatterns = [
    path('', IndexView.as_view()),
    path('lichhoc/', LichHoc.as_view()),
]
