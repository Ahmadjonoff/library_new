from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListCreateAPIView.as_view(), name='books'),
    # path('books/<int:pk>/', BookUpdateDeleteAPIView.as_view(), name='book'),
    # path('api/books/', BookListAPIView.as_view(), name='api-books'),
    # # path('api/books/create/', BookCreateAPIView.as_view(), name='book-create'),

    # path('api/books/<int:pk>/', BookDetailAPIView.as_view(), name='api-book'),
]

urlpatterns += router.urls