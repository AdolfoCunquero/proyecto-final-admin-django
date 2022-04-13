from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.db.models import Count
from .serializers import CategorySerializer, ProductListSerializer
from .models import Category, Product

aviable_databases = ["mysql","postgres","sqlserver"]

def get_database_name(db):
    if db not in aviable_databases or db == "":
        return "postgres"

    return db

class ProductByDatabase(APIView):

    def get(self, request, format=None):
        results = []
        
        for db in aviable_databases:
            results.append({
                "database":db,
                "payload": {
                    "products":Product.objects.using(db).count()
                }
            })

        return Response(results)

class CategoryApiView(APIView):

    def get(self, request, database, format=None):
        db = get_database_name(database)
        cat = Category.objects.using(db).all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)

    def post(self, request, database, format=None):
        created = []
        data = request.data
        
        for db in aviable_databases:
            cat = Category(name=data["name"])
            cat.save(using=db)
            created.append({
                "database":db,
                "payload":{
                    "name":cat.name,
                    "id":cat.id
                }
            })

        return Response(created, status=HTTP_201_CREATED)
        

class ProductApiView(APIView):

    def get(self, request, database, format=None):
        db = get_database_name(database)
        product = Product.objects.using(db).all()
        serializer = ProductListSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, database, format=None):
        db = get_database_name(database)
        data = request.data
        cat = Category.objects.using(db).get(pk=data["category"])

        product = Product(
            category=cat,
            name=data["name"],
            quantity=data["quantity"],
            um= data["um"], 
            purchase_price=data["purchase_price"],
            sale_price=data["purchase_price"]
        )

        product.save(using=db)
        data["id"] = product.id
        return Response(data, status=HTTP_201_CREATED)

class ProductByCategoryApiView(APIView):

    def get(self, request, database,format=None):
        db = get_database_name(database)
        product = Product.objects.using(db).values("category__name").annotate(count=Count("id"))

        return Response(product, HTTP_200_OK)
