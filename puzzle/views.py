from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Puzzle, Company
from .forms import AddPuzzleForm, AddCompanyForm


class HomeListView(ListView):
    model = Puzzle
    template_name = 'puzzle/home.html'

class PuzzleDetail(DetailView):
    model = Puzzle
    template_name = 'puzzle/detail.html'
    context_object_name = 'puzzle'

def add_puzzle(request):
    forms = AddPuzzleForm()
    if request.method == 'POST':
        forms = AddPuzzleForm(request.POST, request.FILES)
        if forms.is_valid():
            cd = forms.cleaned_data
            print(cd)
            company = Company.objects.get(id=int(cd.pop('company')))
            puzzle = Puzzle.objects.create(company=company,**cd)
            #return render(request, 'puzzle/add_puzzle.html', {"forms": forms})
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


# def import_data(request):
#
