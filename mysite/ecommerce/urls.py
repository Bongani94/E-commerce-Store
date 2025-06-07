from django.urls import path
from . views import IndexView, AboutView, ContactView, AuthorBooksView, BrowseBookView, NewArrivalsView, BestSellersView, CategoryBooksView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('authors/', AuthorBooksView.as_view(), name='author_books'),
    path('browse/', BrowseBookView.as_view(), name='browse_book'),
    path('new_arrivals/', NewArrivalsView.as_view(), name='new_arrivals'),
    path('best_sellers/', BestSellersView.as_view(), name='best_sellers'),
    path('category/', CategoryBooksView.as_view(), name='category_books'),
]  
