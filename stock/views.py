from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from .permissions import CustomModelPermission
from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Transaction
)
from .serializers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    FirmSerializer,
    TransactionSerializer,
    CategoryProductsSerializer
)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [DjangoModelPermissions] 
    '''
    since the default DjangoModelPermissions does not have any restrictions on GET methods (you can see that by 
    going into the source code) we will write our own permission, CustomModelPermission, and use it instead
    '''
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['name']

    '''
    Why are we overriding get_serializer_class? Since we have defined a nested serializer CategoryProductsSerializer we only want
    to get access to this only when we filter or search that category. Therefore, in the endpoint /stock/category/ when we filter 
    or search the category, say, Shoes, our endpoint automatically changes to stock/category/?name=Shoes. How can we determine 
    what's being filtered or searched you might be wondering. Well, query_params is what you need. Therefore having a dictionary 
    at hand we can determine it by self.request.query_params.get('name')
    '''
    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            return CategoryProductsSerializer # only if we have an endpoint with name filtered/searched will we use CategoryProductsSerializer, which is nested
        else:
            return super().get_serializer_class() # else, return the super serializer, that is, as defined above in th line 23, CategorySerializer

class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name']

class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['firm', 'transaction', 'product']
    search_fields = ['firm']

    def perform_create(self, serializer): # we are saving the user with perform_create. see more here: https://www.django-rest-framework.org/api-guide/generic-views/#methods
        serializer.save(user=self.request.user)