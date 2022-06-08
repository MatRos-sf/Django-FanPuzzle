from django.test import TestCase, Client
from django.urls import reverse
from puzzle.models import Puzzle, Company

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.company_one = Company.objects.create(name='TestCompanyOne')
        self.company_two = Company.objects.create(name='TestCompanyOneTwo',
                                                  fullname= 'FullnameTestCompanyOneTwo',
                                                  description= 'Description TestCompanyOneTwo')
        self.puzzle_one = Puzzle.objects.create(name='TestPuzzleOne',
                                                number_of_pieces=150,
                                                ean_code="123456789",
                                                company=self.company_one,
                                                product_code= "123456789")
        self.puzzle_two = Puzzle.objects.create(name='TestPuzzleTwo',
                                                number_of_pieces=1050,
                                                ean_code="987654321",
                                                company=self.company_one,
                                                product_code="987654321")

    def test_settings(self):
        self.assertEqual(Company.objects.count(),2)
        self.assertEqual(Puzzle.objects.count(),2)

        amount_puzzle_in_company = Company.objects.get(pk=1).puzzles.count()
        self.assertEqual(amount_puzzle_in_company, 2)

    def test_home_views_get(self):
        response =  self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response, 'puzzle/home.html')