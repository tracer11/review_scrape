from django.db import models


#fields = {title of the review: Char, the content of review: TextField, author: Char, star rating : float, date of review : date , closed with lender : bool }
# Create your models here.
class Review(models.Model):
  title = models.CharField(max_length=250)
  content = models.TextField(max_length=1000)
  author = models.CharField(max_length=250)
  star_rating = models.CharField(max_length=250)
  date_of_review = models.CharField(max_length=250)


    