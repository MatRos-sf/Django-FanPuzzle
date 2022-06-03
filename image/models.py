from django.db import models


class Image(models.Model):

    user = models.ForeignKey('accounts.Account',
                             related_name='user_photos',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='user_photo/',
                              db_index=True)
    photo_like = models.ManyToManyField('accounts.Account',
                                        related_name='photo_like',
                                        blank=True)
    def __str__(self):
        return self.title

class ProfilePhoto(models.Model):
    user = models.OneToOneField('accounts.Account',
                             related_name='user_profile_photo',
                             on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='user_profile_photo/',
                              default='user_profile_photo/default.jpg'
                              )


