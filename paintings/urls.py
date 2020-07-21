from django.urls import path

from .views import PaintingList, PaintingDetail

urlpatterns = [
    path('', PaintingList.as_view()),
    path('<int:pk>/', PaintingDetail.as_view()),
]
