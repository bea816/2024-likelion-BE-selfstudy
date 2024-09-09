from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

from .models import *
from .serializers import *

"""
CBV
class HelloAPI(APIView):
    def get(self, request):
        return Response("hello world")
"""

# FBV
# get 요청을 받을 수 있는 api라 표기
@api_view(['GET']) 
def HelloAPI(request):
    """
    request는 사용자가 보낸 요청의 타입(get, post, ...), 사용자가 어떤 데이터를 보냈는지에 대한 정보
    request.method: 요청의 타입 알아내기
    request.data: 데이터 얻기  

    Response는 drf의 결과 반환 방식
    Response: 응답에 대한 정보
    response.data: 응답에 포함되는 데이터
    response.status: 응답에 대한 상태
    """
    return Response("hello world!")

"""
FBV
"""

@api_view(['GET', 'POST'])
def booksAPI(request): # api 주소 > /book/
    if request.method == 'GET':
        books = Book.objects.all() # Book 모델에서 전체 데이터 가져오기
        serializer = BookSerializer(books, many=True) # many=True는 여러 데이터 처리 가능하도록
        # 데이터 한번에 집어 넣기
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        # post 요청으로 들어온 데이터를 시리얼라이저에 집어넣기
        if serializer.is_valid():
            serializer.save() # create 함수 동작
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookAPI(request, bid): # api 주소 > /book/bid/
    book = get_object_or_404(Book, bid=bid)
    # bid = id인 데이터를 book에서 가져오고, 없으면 404 에러
    serializer = BookSerializer(book) # 데이터 직렬화
    return Response(serializer.data, status=status.HTTP_200_OK)

"""
CBV
"""
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)