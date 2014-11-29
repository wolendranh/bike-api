from django.db import models

# Create your models here.


class Place(models.Model):
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    home_page = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=4)
    longitude = models.DecimalField(max_digits=20, decimal_places=4)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100)
    work_time = models.TextField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(max_length=100)


class Comment(models.Model):
    place = models.ForeignKey(Place, related_name='comments')
    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    like = models.BooleanField(default=False)
    date = models.DateTimeField(auto_created=True)


class StolenBike(models.Model):
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    model = models.CharField(max_length=100)
    photo = models.ImageField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField()


class BicycleLine(models.Model):
    street = models.CharField(max_length=50)
    first_latitude = models.DecimalField(max_digits=20, decimal_places=4)
    first_longitude = models.DecimalField(max_digits=20, decimal_places=4)
    second_latitude = models.DecimalField(max_digits=20, decimal_places=4)
    second_longitude = models.DecimalField(max_digits=20, decimal_places=4)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField()
    line_path = models.CharField(max_length=300)



