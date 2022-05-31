from django.test import TestCase
from puzzle.models import Puzzle, Company

class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(name='Test')
    def test_default_model(self):
        """Did the model be create?"""
        m = Company.objects.all()
        self.assertEqual(m.count(),1)
        self.assertEqual(m.get(pk=1).name, 'Test')
    def test_create_company_fail_name(self):
        """ Why create empty name Models!"""
        payload = {
            'fullname': 'Test2Django',
            'description': 'Simple test',
            'country': 'Poland',
            'city': 'Gdynia'
        }
        company = Company.objects.create(**payload)
        self.assertEqual(Company.objects.count(), 2)



