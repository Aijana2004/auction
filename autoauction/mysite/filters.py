from django_filters import FilterSet
from .models import Car


class CarFilter(FilterSet):
    class Mets:
        models = Car
        filed = {
            'price':['gt','lt'],
            'model':['exact'],
            'year': ['exact'],
            'brand': ['exact'],
            'fuel_type': ['exact'],
            'transmission': ['exact']

        }
