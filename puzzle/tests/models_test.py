from django.db import IntegrityError
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
    def test_create_company_name(self):
        """
        Why create empty name Models!
        https://stackoverflow.com/questions/51148893/object-created-even-if-field-was-required
        """
        payload = {
            'name': '',
            'fullname': 'Test2Django',
            'description': 'Simple test',
            'country': 'Poland',
            'city': 'Gdynia'
        }
        company = Company.objects.create(**payload)
        self.assertEqual(Company.objects.count(), 2)
    # def test_create_company_the_samme_name(self):
    #     payload = {
    #         'name': 'Test',
    #         'fullname': 'Test2Django',
    #         'description': 'Simple test',
    #         'country': 'Poland',
    #         'city': 'Gdynia'
    #     }
    #
    #     # with self.assertRaises(IntegrityError):
    #     #     Company.objects.create(**payload)
    #     try:
    #         company = Company.objects.create(**payload)
    #     except IntegrityError:
    #         company = False
    #     #self.assertEqual(company, False)
    #     self.assertEqual(Company.objects.count(),1)

    def test_delete_model(self):
        company = Company.objects.get(id=1)
        company.delete()
        self.assertEqual(Company.objects.count(),0)
    def test_edit_model(self):
        company = Company.objects.get(id=1)
        company.name = 'NewTest'
        company.description = 'Simple Test'
        company.save()
        self.assertEqual([company.name, company.description],
                         ['NewTest', 'Simple Test'])



