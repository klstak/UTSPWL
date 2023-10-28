# backend/views.py

from pyramid.view import view_config
from pyramid.response import Response
import json

PRODUCTS = [
    {"id": 1, "name": "Produk 1", "price": 10, "stock": 100},
    {"id": 2, "name": "Produk 2", "price": 20, "stock": 50},
    # Tambahkan data produk lainnya di sini
]

@view_config(route_name='get_products', renderer='json')
def get_products(request):
    return PRODUCTS

@view_config(route_name='add_product', request_method='POST', renderer='json')
def add_product(request):
    data = json.loads(request.body)
    # Validasi dan tambahkan produk baru ke PRODUCTS
    # ...
    return Response("Produk berhasil ditambahkan")

@view_config(route_name='delete_product', request_method='POST', renderer='json')
def delete_product(request):
    data = json.loads(request.body)
    product_id = data["id"]
    # Hapus produk dengan product_id dari PRODUCTS
    # ...
    return Response("Produk berhasil dihapus")
