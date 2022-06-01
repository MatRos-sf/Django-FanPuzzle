from django.db import models
from django.urls import reverse
class Company(models.Model):

    name = models.CharField(max_length=150, unique=True, blank=False)

    fullname = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=False)
    #https://pypi.org/project/django-countries/
    country = models.CharField(max_length=100, blank=True, null=True)
    #https://github.com/coderholic/django-cities
    city = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=500, blank=True, null=True)
    image =  models.ImageField(upload_to='company/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-update', args=[self.pk])


class Points(models.Model):

    for_add = models.IntegerField(default=0)
    for_daily_login = models.IntegerField(default=1)
    for_comments = models.IntegerField(default=0)
    for_edit = models.IntegerField(default=0)
    for_like = models.IntegerField(default=0)
    for_visit = models.IntegerField(default=0)
    for_bonus = models.IntegerField(default=0)

    def sum_points(self):
        return sum([self.for_add, self.for_daily_login, self.for_comments, self.for_edit, self.for_like,
                     self.for_visit, self.for_bonus])
    def __str__(self):
        return f"{self.sum_points()}"



class Puzzle(models.Model):

    name = models.CharField(max_length=200)
    number_of_pieces = models.IntegerField()
    ean_code = models.CharField(max_length=13, unique=True)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='puzzles')
    product_code = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    #https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg
    likes = models.ManyToManyField("accounts.Account", related_name='puzzle_like', blank=True)
    to_do = models.ManyToManyField("accounts.Account", related_name='to_do', blank=True)
    #points
    #points = models.OneToOneField

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super(Puzzle, self).delete()

    def number_of_likes(self):
        return self.likes.count()

    def number_of_to_do(self):
        return self.to_do.count()

    class Meta:
        ordering = ('-created',)



    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     # when we upgrade new image old have to delete
    #     try:
    #         old_image = Puzzle.objects.get(id=self.pk)
    #         if old_image.image != self.image:
    #             old_image.image.delete()
    #     except:     pass
    #     super(Puzzle, self).save()

