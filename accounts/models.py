from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#ma@wp.pl
#https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#specifying-a-custom-user-model

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):  #must add all REQUIRED_FIELDS
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email= self.normalize_email(email),
            password = password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class Points(models.Model):

    for_add = models.IntegerField(default=0)
    amt_adds = models.IntegerField(default=0)

    for_daily_login = models.IntegerField(default=1)

    for_comments = models.IntegerField(default=0)
    amt_comments = models.IntegerField(default=0)

    for_edit = models.IntegerField(default=0)
    amt_edits = models.IntegerField(default=0)

    for_like = models.IntegerField(default=0)
    amt_likes = models.IntegerField(default=0)

    for_visit = models.IntegerField(default=0)
    amt_visits = models.IntegerField(default=0)

    for_bonus = models.IntegerField(default=0)


    def sum_points(self):
        return sum([self.for_add, self.for_daily_login, self.for_comments, self.for_edit, self.for_like,
                     self.for_visit, self.for_bonus])
    def __str__(self):
        return f"{self.sum_points()}"

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name='email')
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    #Profile
    description = models.TextField(max_length=800,blank=True, null=True)
    #Warring if you makemigrations model first time this doesnt work!!
    points = models.OneToOneField(Points, on_delete=models.CASCADE)
    # user Image



    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # profile picture , add fotoo,
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']          #co jest nam potrzebne

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.points = Points.objects.create()

        super().save(*args,**kwargs)


