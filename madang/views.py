from django.shortcuts import render,redirect, get_object_or_404
from .models import Madang
# Create your views here.
def main(request):
    return render(request, 'madang/madang.html')

def map_detail(request, pk):
    madang = get_object_or_404(Madang, pk=pk)
    return render(request, 'madang/madang_detail.html', {'madang':madang})