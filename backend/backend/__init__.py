# backend/__init__.py

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_jinja2")
    config.add_static_view(name="static", path="static", cache_max_age=3600)
    config.add_route('get_products', '/get_products')
    config.add_route('add_product', '/add_product')
    config.add_route('delete_product', '/delete_product')
    config.scan()
    return config.make_wsgi_app()
