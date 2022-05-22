from .models import Puzzle, Company
from django import forms



class AddCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'

class AddPuzzleForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(), required=False)
    number_of_pieces = forms.CharField(widget=forms.TextInput())
    ean_code = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    #company = forms.ChoiceField(choices=COMPANIES)
    product_code = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField(required=False)
    class Meta:
        model = Puzzle
        fields = ["name", "number_of_pieces", "ean_code", "description", "product_code", "image", 'company']

    # def clean_name(self):
    #     cd = super().clean()
    #     name = cd.get('name')
    #     if not name:
    #         self.add_error('name','Hello write name !!')
    #     return cd

class UrlJumbo(forms.Form):
    url = forms.CharField(required=False)
    #must be: https://www.jumbo.eu/en/products/

    def clean(self):
        cd = super().clean()
        #replace in case if client write "htt ps: //www .jum bo. eu/en /produc ts/falcon-the-veg etable-garden-1000- pieces /"
        url = cd.get('url').replace(" ","")
        print(url)
        if not url:
            self.add_error('url', "Please, Paste Jumbo website url")
        if not "https://www.jumbo.eu/en/products/" in url:
            self.add_error('url', 'Jumbo website begins: "https://www.jumbo.eu/en/products/..." ')
        if url.count('/') != 6:
            self.add_error('url', 'Check your link. The link must include 6 char: "/"')
        return cd
