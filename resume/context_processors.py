from django.shortcuts import get_object_or_404

from .models import StaticAssets

def last_updated(request):
    return {
        'last_updated': get_object_or_404(
            StaticAssets,
            reference_name="last_updated").value
    }

def source_code(request):
    return {
        'source_code': get_object_or_404(StaticAssets, reference_name="sourcecode").value
    }