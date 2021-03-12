from django.http import HttpResponse
from rest_framework import viewsets
from .models import Review
from .serializer import ReviewSerializer
from bs4 import BeautifulSoup

import requests
import json

# Create your views here.

class ReviewAPI(viewsets.ModelViewSet):
  queryet = Review.objects.all()
  serializer_class = ReviewSerializer

#check to see if url is valid
def url_works(url):
  if url.ok:
    return True
  else:
    return False


def scrape(request):
  page_count = 1
  def paginate(page_count):
    url = f'https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183?sort=cmV2aWV3c3VibWl0dGVkX2Rlc2M=&pid={page_count}'
    page = requests.get(url)
    if url_works(page) == True:
      soup = BeautifulSoup(page.content, 'html.parser')
      results_review = soup.find(class_='lenderReviews')
      elems = results_review.find_all(class_='col-xs-12 mainReviews')
      elems += results_review.find_all(class_='col-xs-12 mainReviews hiddenReviews')
      
      for elem in elems:
        review = Review()
        review.title = elem.find('p', class_='reviewTitle').text.strip()
        review.contetn = elem.find('p', class_='reviewText').text.strip()
        review.author = elem.find('p', class_='consumerName').text.strip()
        review.star_rating = elem.find('div', class_='numRec').text.strip()
        review.date_of_review = elem.find('p', class_='consumerReviewDate').text.strip()

      results_page = soup.find(class_='lenderNav pagination')
      next_page = results_page.find_all('li', class_='page-item')
      
      for page in next_page:
        next_ = page.find('a', class_='page-link')['aria-label'] == 'Next Page'
      
      if next_ == True:
        page_count += 1
        paginate(page_count)
      else:
        return HttpResponse("Fetched all reviews")
    else:
      print("url broken")
  paginate(page_count)


