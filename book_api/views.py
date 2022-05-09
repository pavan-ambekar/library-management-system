from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Book
from .serializer import BookSerializer

#  Create your views here.


class GetBooks(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class AddBook(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetails(APIView):

    def getBookByPK(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({'error': 'Book does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        book = self.getBookByPK(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.getBookByPK(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.getBookByPK(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
