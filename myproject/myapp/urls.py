from django.urls import path
from .views import UserCreateAPI ,ProductAPI,LeadAPI,LeadDateAPI,TopProductAPI,BottomProductAPI,ProductLeadInquiryAPI
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
    path('signup-api/',UserCreateAPI.as_view()),
    path('access-token-api/',TokenObtainPairView.as_view()),
    path('refresh-token-api/',TokenRefreshView.as_view()),



    path('product-api/',ProductAPI.as_view()),
    path('product-api/<int:pk>/',ProductAPI.as_view()),

    path('lead-api/',LeadAPI.as_view()),
    path('lead-date-api/',LeadDateAPI.as_view()),
    path('top-product-api/',TopProductAPI.as_view()),
    path('bottom-product-api/',BottomProductAPI.as_view()),
    path('product-inquiry-api/',ProductLeadInquiryAPI.as_view())


]