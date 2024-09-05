from drf_yasg import openapi

api_info = openapi.Info(
    title="Product Lead Management API",
    default_version='v1',
    description="This is the API documentation for the Product and Lead Management system. The API allows for full CRUD operations on products, creating leads, and generating reports on leads and products.",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="bijwerohit9@gmail.com"),
    license=openapi.License(name="BSD License"),
)