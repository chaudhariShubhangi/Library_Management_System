from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import datetime
from .models import Book
from .serializer import BookSerializer


class retreive_books(APIView):
    try:
        def get(self,request):
            requested_data = request.data
            book_name = requested_data['book_name']
            author_name = requested_data['author_name']
            category =requested_data['category']
            today = datetime.date.today()

            queryset = Book.objects.filter(book_name = book_name, author_name = author_name , category = category,added_date = today)
            serializer = BookSerializer(data = queryset)
            serializer.is_valid()
            result = {
                "result" : serializer.data,
                "message" : "Books Fetched Successfully",
                "status" : status.HTTP_200_OK
            }

            return Response(result)

        def post(self,request):
            requested_data = request.data
            book_name = requested_data['book_name']
            author_name = requested_data['author_name']
            category = requested_data['category']
            today = datetime.date.today()
            print(today)

            obj = Book.objects.create(book_name = book_name, author_name = author_name , category = category,added_date = today)
            serializer = BookSerializer(data = obj)
            if serializer.is_valid():
                serializer.save()
                result = {
                    "message": "Books Created Successfully",
                    "status": status.HTTP_201_CREATED
                }
                return Response(result)
            else:
                result = {
                    "message": "Invalid Data",
                    "status": status.HTTP_201_CREATED
                }
                return Response(result)

    except Exception as e:
        print(str(e))



# class CreateUpdateDelete(APIView):
#     try:
#         def post(self,request):
#
#
#     except Exception as e:
#         print(str(e))

