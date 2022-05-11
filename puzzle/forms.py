from .models import Puzzle, Company
from django import forms

COMPANIES = [(i.id, i) for i in Company.objects.all()]
# class AddCompany(forms.ModelForm):
#     class Meta:
#         model = Company
#         field = '__all__'

class AddPuzzleForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=False)
    number_of_pieces = forms.CharField(widget=forms.TextInput())
    ean_code = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())
    company = forms.ChoiceField(choices=COMPANIES)
    product_code = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField(required=False)
    class Meta:
        model = Puzzle
        fields = ["name", "number_of_pieces", "ean_code", "description", "product_code", "image"]

    # def clean_name(self):
    #     cd = super().clean()
    #     name = cd.get('name')
    #     if not name:
    #         self.add_error('name','Hello write name !!')
    #     return cd

class UrlJumbo(forms.Form):
    url = forms.CharField()
    #must be: https://www.jumbo.eu/en/products/