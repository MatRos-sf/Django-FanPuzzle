from django.urls import path
from .views import HomeListView, PuzzleDetail, add_puzzle, add_company, import_data, update_puzzle, search_puzzle, search_navibar, update_company, CompanyDetail
from django.conf.urls.static import static
from django.conf import settings

#app_name = 'my_app'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('add/', add_puzzle, name='puzzle-add'),
    path('add_company/', add_company, name='puzzle-add-company' ),
    path('detail/<int:pk>/', PuzzleDetail.as_view(), name='puzzle-detail'),
    path('detail/company/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('import/', import_data, name='import'),
    path('update/puzzle/<int:pk>/', update_puzzle, name='puzzle-update'),
    path('update/company/<int:pk>/', update_company, name='company-update'),
    path('list/$', search_puzzle, name='search'),
    path('search/', search_navibar, name='search-navi'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)