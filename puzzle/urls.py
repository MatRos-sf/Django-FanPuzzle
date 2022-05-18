from django.urls import path
from .views import HomeListView, PuzzleDetail, add_puzzle, add_company, import_data, update_puzzle
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('add/', add_puzzle, name='puzzle-add'),
    path('add_company/', add_company, name='puzzle-add-company' ),
    path('detail/<int:pk>/', PuzzleDetail.as_view(), name='puzzle-detail'),
    path('import/', import_data, name='import'),
    path('update/<int:pk>/', update_puzzle, name='puzzle-update')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)