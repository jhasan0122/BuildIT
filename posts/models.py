from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    post_pic1 = models.ImageField(default='empty.jpg',upload_to='post-pic1')
    post_pic2 = models.ImageField(default='empty.jpg',upload_to='post-pic2')
    post_pic3 = models.ImageField(default='empty.jpg',upload_to='post-pic3')
    post_pic4 = models.ImageField(default='empty.jpg',upload_to='post-pic4')
    post_pic5 = models.ImageField(default='empty.jpg',upload_to='post-pic5')
    post_pic6 = models.ImageField(default='empty.jpg',upload_to='post-pic6')
    address = models.CharField(max_length=100,default='')
    price = models.IntegerField(default=0)
    use_for = models.IntegerField(default=0)
    map = models.CharField(max_length=400, default='')
    MSZoning = models.CharField(max_length=50, default='')
    LotFrontage = models.IntegerField(default=0)
    LotArea = models.IntegerField(default=0)
    BldgType = models.CharField(max_length=50, default='')
    OverallQual = models.CharField(max_length=50, default='')
    OverallCond = models.CharField(max_length=50, default='')
    YearBuilt = models.IntegerField(default=0)
    RoofStyle = models.CharField(max_length=50, default='')
    RoofMatl = models.CharField(max_length=50, default='')
    Exterior1st = models.CharField(max_length=50, default='')
    Exterior2nd = models.CharField(max_length=50, default='')
    ExterQual = models.CharField(max_length=50, default='')
    ExterCond = models.CharField(max_length=50, default='')
    Foundation = models.CharField(max_length=50, default='')
    BsmtQual = models.CharField(max_length=50, default='')
    BsmtCond = models.CharField(max_length=50, default='')
    TotalBsmtSF = models.IntegerField(default=0)
    CentralAir = models.CharField(max_length=50, default='')
    FirstFlrSF = models.IntegerField(default=0)
    SecondFlrSF = models.IntegerField(default=0)
    GrLivArea = models.IntegerField(default=0)
    KitchenQual = models.CharField(max_length=50, default='')
    TotRmsAbvGrd = models.IntegerField(default=0)
    GarageType = models.CharField(max_length=50, default='')
    GarageCars = models.IntegerField(default=0)
    GarageArea = models.IntegerField(default=0)
    GarageQual = models.CharField(max_length=50, default='')
    GarageCond = models.CharField(max_length=50, default='')
    PoolArea = models.IntegerField(default=0)
    MiscVal = models.IntegerField(default=0)

    SaleType = models.CharField(max_length=50,default='')
    SaleCondition = models.CharField(max_length=50, default='')


    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})