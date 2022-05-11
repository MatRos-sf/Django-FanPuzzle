from django.urls import path
from .views import HomeListView, PuzzleDetail, add_puzzle
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('add/', add_puzzle, name='puzzle-add'),
    path('detail/<int:pk>/', PuzzleDetail.as_view(), name='puzzle-detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)