from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.http import HttpResponse

@login_required
def image_create(request):
    if request.method == 'POST':
        # Formularz został wysłany.
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # Dane formularza są prawidłowe.
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # Przypisanie bieżącego użytkownika do elementu.
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Obraz został dodany.')
            # Przekierowanie do widoku szczegółowego dla nowo utworzonego elementu.
            #return redirect(new_item.get_absolute_url())
            return HttpResponse("<h1>;)</h1>")
    else:
        # Utworzenie formularza na podstawie danych dostarczonych przez bookmarklet w żądaniu GET.
        form = ImageCreateForm(data=request.GET)

    return render(request,
                  'image/create.html',
                  {'section': 'images',
                   'form': form})