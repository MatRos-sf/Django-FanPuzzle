from django.test import SimpleTestCase
from django.urls import reverse, resolve
from puzzle import views

class TestUrls(SimpleTestCase):
    """
    resolve(url)
    (func=puzzle.views.add_company, args=(), kwargs={}, url_name='puzzle-add-company', app_names=[], namespaces=[], route='add_company/')

    """
    def test_home_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, views.HomeListView)
    def test_add_puzzle_resolves(self):
        url = reverse('puzzle-add')
        self.assertEqual(resolve(url).func, views.add_puzzle)
    def test_add_company_resolves(self):
        url = reverse('puzzle-add-company')
        self.assertEqual(resolve(url).func, views.add_company)
    def test_detail_resolves(self):
        url = reverse('puzzle-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.PuzzleDetail)
    def test_detail_company_resolves(self):
        url = reverse('company-detail',args=[2])
        self.assertEqual(resolve(url).func.view_class, views.CompanyDetail)
    def test_import_resolves(self):
        url = reverse('import')
        self.assertEqual(resolve(url).func, views.import_data)
    def test_update_company_resolves(self):
        url = reverse('company-update', args=[3])
        self.assertEqual(resolve(url).func, views.update_company)
    def test_search_resolves(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, views.search_puzzle)
    def test_search_navibar_resolves(self):
        url = reverse('search-navi')
        self.assertEqual(resolve(url).func, views.search_navibar)