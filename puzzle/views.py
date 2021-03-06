from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Puzzle, Company
from .forms import AddPuzzleForm, AddCompanyForm, UrlJumbo
from .information_with_website.jumbo import information_with_jumbo
from django.http import HttpResponse
#errors
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

class HomeListView(ListView):
    model = Puzzle
    template_name = 'puzzle/home.html'

class PuzzleDetail(DetailView):
    model = Puzzle
    template_name = 'puzzle/detail.html'
    context_object_name = 'puzzle'

class CompanyDetail(DetailView):
    model = Company
    template_name = 'puzzle/detail_company.html'
    context_object_name = 'company'

def add_puzzle(request):
    forms = AddPuzzleForm()
    if request.method == 'POST':
        forms = AddPuzzleForm(request.POST, request.FILES)
        if forms.is_valid():
            cd = forms.cleaned_data
            company = cd.pop('company')
            puzzle = Puzzle.objects.create(company=company,**cd)
            return redirect('puzzle-detail', pk=puzzle.pk)
        else:
            return render(request, 'puzzle/add_puzzle.html', {"forms": forms})
    else:
        return render(request, 'puzzle/add_puzzle.html', {"forms": forms})

def add_company(request):
    #I use the same template: add_puzzle
    forms = AddCompanyForm()
    if request.method == 'POST':
        forms = AddCompanyForm(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            company = Company.objects.create(**cd)
            return redirect('home')
        else:
            return render(request, 'puzzle/add_puzzle.html', {"forms": forms})
    else:
        return render(request, 'puzzle/add_puzzle.html', {"forms": forms})

# import from Jumbo
def import_data(request):
    forms = UrlJumbo()
    if request.method == 'GET':
        print(1)
    if request.method == 'POST':
        forms = UrlJumbo(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            detail_information = information_with_jumbo(cd['url'])
            # create model
            try:
                company_model = Company.objects.get(name=detail_information.pop('company'))
            except ObjectDoesNotExist:
                return HttpResponse("We support only company: .....")
            # create model
            try:
                p = Puzzle.objects.create(company=company_model, **detail_information)
            except IntegrityError:
                p = Puzzle.objects.get(ean_code=detail_information['ean_code'])
                return HttpResponse(f"{p} exist")

            return redirect('puzzle-detail', pk=p.id)
        else:
            return render(request, 'puzzle/import/jumbo.html', {'forms': forms})
    else:
        return render(request, 'puzzle/import/jumbo.html', {'forms': forms})


#edit
## Puzzle
def update_puzzle(request, pk):
    p = get_object_or_404(Puzzle, pk=pk)
    form = AddPuzzleForm(request.POST or None, request.FILES or None, instance=p)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('puzzle-detail', pk=p.pk)
        else:
            return HttpResponse("<h1>Smth is wrong </h1>")
    else:
        return render(request, 'puzzle/update.html', {'forms': form})

## Company

def update_company(request,pk):
    c = get_object_or_404(Company, pk=pk)
    form = AddCompanyForm(request.POST or None, instance= c)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('company-detail', pk=c.pk)
        else:
            return HttpResponse("<h1>Smth is wrong </h1>")
    else:
        return render(request, 'puzzle/update.html', {'forms': form})

from .filters import PuzzleFilter
def search_puzzle(request):
    f = PuzzleFilter(request.GET, queryset=Puzzle.objects.all())
    return render(request, 'puzzle/search.html', {'filter': f})

def search_navibar(request):
    # I wll do: About 4,930,000,000 results (0.69 seconds)
    if request.method == 'GET':
        name = request.GET['name']
        searched = Puzzle.objects.filter(name__contains=name)
        print(searched.count())

        return render(request, 'puzzle/simple_search.html', {'searched': searched,
                                                             'name': name})

    return render(request, 'puzzle/simple_search.html', {})