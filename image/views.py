from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.http import HttpResponse

@login_required
def image_create(request):
    if request.method == 'POST':
        # Formularz został wysłany.
        forms = ImageCreateForm(request.POST, request.FILES)
        if forms.is_valid():
            # Dane formularza są prawidłowe.
            cd = forms.cleaned_data
            print(cd)
            new_item = forms.save(commit=False)
            print(2)
            # Przypisanie bieżącego użytkownika do elementu.
            new_item.user = request.user
            new_item.save()
            print("add photo")
            messages.success(request, 'Obraz został dodany.')
            # Przekierowanie do widoku szczegółowego dla nowo utworzonego elementu.
            #return redirect(new_item.get_absolute_url())
            return HttpResponse("<h1>;)</h1>")
    else:
        # Utworzenie formularza na podstawie danych dostarczonych przez bookmarklet w żądaniu GET.
        forms = ImageCreateForm(data=request.GET)

    return render(request,
                  'image/create.html',
                  {'section': 'images',
                   'forms': forms})