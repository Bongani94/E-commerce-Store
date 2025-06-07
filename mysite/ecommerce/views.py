from django.views import generic
from . models import Book, Author, Category, Review, CartItem, User

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        """Return the last five published books."""
        return Book.objects.order_by('-publication_date')[:5]
    
    
class AboutView(generic.TemplateView):
    template_name = 'about.html'    
    
class ContactView(generic.TemplateView):
    template_name = 'contact.html'
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Feel free to reach out to us!"
        return context
    
class AuthorBooksView(generic.ListView):
    template_name = 'author_books.html'
    context_object_name = 'books_by_author'

    def get_queryset(self):
        """Return books by a specific author."""
        author_slug = self.kwargs['slug']
        return Book.objects.filter(author__slug=author_slug).order_by('-publication_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.kwargs['slug']
        return context
    
class BrowseBookView(generic.DetailView):
    model = Book
    template_name = 'browse_book.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_books'] = Book.objects.filter(category=self.object.category).exclude(id=self.object.id)[:5]
        return context
    
class NewArrivalsView(generic.ListView):
    template_name = 'new_arrivals.html'
    context_object_name = 'new_arrivals_list'

    def get_queryset(self):
        """Return the last five published books."""
        return Book.objects.order_by('-publication_date')[:5]

class BestSellersView(generic.ListView):
    template_name = 'best_sellers.html'
    context_object_name = 'best_sellers_list'

    def get_queryset(self):
        """Return the top 5 best-selling books."""
        return Book.objects.order_by('-stock_quantity')[:5]
    
class CategoryBooksView(generic.ListView):
    template_name = 'category.html'
    context_object_name = 'books_by_category'

    def get_queryset(self):
        """Return books in a specific category."""
        category_slug = self.kwargs['slug']
        return Book.objects.filter(category__slug=category_slug).order_by('-publication_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['slug']
        return context