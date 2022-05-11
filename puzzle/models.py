from django.db import models
class Company(models.Model):

    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Puzzle(models.Model):
    name = models.CharField(max_length=200)
    number_of_pieces = models.IntegerField()
    ean_code = models.CharField(max_length=13, unique=True)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='puzzles')
    product_code = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    #website
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

