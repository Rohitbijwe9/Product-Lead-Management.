from django.shortcuts import render
from . models import Product,Lead
from . serializer import ProductSerializer,LeadSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import User,UserSerializer
from django.utils.dateparse import parse_date
from .permission import IsAuthenticatedForMethodsExceptGet  
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema




class UserCreateAPI(APIView):
    permission_classes=[AllowAny]

    @swagger_auto_schema(
        operation_description="Create a new user",
        request_body=UserSerializer,
        responses={201: UserSerializer, 400: "Bad Request"},
    )

    def post(self,request):
        try:
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({'message':'user create succesully...'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    




class ProductAPI(APIView):

    permission_classes = [IsAuthenticatedForMethodsExceptGet]
    @swagger_auto_schema(
        operation_description="Create a new product",
        request_body=ProductSerializer,
        responses={201: ProductSerializer, 400: "Bad Request"},
    )
    def post(self,request):
        try:
            serializer=ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({'message':'data save succesully...'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Retrive all products",
        responses={200: ProductSerializer(many=True), 400: "Bad Request"},
    )
    def get(self,request):
        try:
            product=Product.objects.all()
            serializer=ProductSerializer(product,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        


    @swagger_auto_schema(
        operation_description="product update succefully",
        request_body=ProductSerializer,
        responses={201: ProductSerializer, 400: "Bad Request", 404: 'Product not found'},
    )
    def put(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Data updated successfully...'}, status=status.HTTP_200_OK)
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="product partially update",
        request_body=ProductSerializer,
        responses={201: ProductSerializer, 400: "Bad Request",404: 'Product not found'
},
    )   
    def patch(self,request,pk):
        try:
            product=Product.objects.get(id=pk)
            serializer=ProductSerializer(product,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response({'message':'data update succesully...'},status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="product delete",
        responses={200: 'product edeleted', 400: "Bad Request",404: 'Product not found'
},
    ) 
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)  # Use pk instead of id
            product.delete()
            return Response({'message': 'Data deleted successfully...'}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LeadAPI(APIView):
   permission_classes = [AllowAny]

   
   @swagger_auto_schema(
        operation_description="Lead create",
        request_body=LeadSerializer,
        responses={201: LeadSerializer, 400: "Bad Request"},
    )

    
   def post(self, request):
        try:
            serializer = LeadSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Lead created successfully.'}, status=status.HTTP_201_CREATED)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
class LeadDateAPI(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Lead date api for fetch between date data",
        request_body=LeadSerializer,
        responses={200: LeadSerializer, 400: "Bad Request"},
    )

    def post(self, request):
        try:
            start_date = request.data.get('start_date')
            end_date = request.data.get('end_date')

            if not start_date or not end_date:
                return Response({'error': 'start_date and end_date are required'}, status=status.HTTP_400_BAD_REQUEST)
            
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)

            if not start_date or not end_date:
                return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
            
            if start_date > end_date:
                return Response({'error': 'start_date must be before end_date.'}, status=status.HTTP_400_BAD_REQUEST)

            leads = Lead.objects.filter(created_at__range=[start_date, end_date])
            serializer = LeadSerializer(leads, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ValueError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class TopProductAPI(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrive Top 10 Product",
        responses={200: ProductSerializer(many=True), 400: "Bad Request"},
    )

    def get(self, request):
        try:
            products = Product.objects.annotate(lead_count=Count('leads')).order_by('-lead_count')[:10]
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

class BottomProductAPI(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retive Bottom 10 Product List",
        responses={200: ProductSerializer(many=True), 400: "Bad Request"},
    )
    def get(self, request):
        try:
            products = Product.objects.annotate(lead_count=Count('leads')).order_by('lead_count')[:10]
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    
class ProductLeadInquiryAPI(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
    operation_description="Product inquiry and their lead counts",
    manual_parameters=[
        openapi.Parameter('param_name', openapi.IN_QUERY, description="description", type=openapi.TYPE_STRING)
    ],
    responses={200: "Successful operation", 400: "Bad Request"},
)
    def get(self, request):
        leads = Lead.objects.annotate(product_count=Count('interested_products'))
        lead_data = [{'lead_name': lead.name, 'product_count': lead.product_count} for lead in leads]
        return Response(lead_data)




