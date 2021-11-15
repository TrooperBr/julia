from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import *



class ProdutsList(ListView):
	model = Produto
	template_name = 'products_list.html'
	context_object_name = 'produtos'
	paginate_by = 3

	




class ProductDetail(DetailView):
	model = Produto
	template_name = 'product.html'
	context_object_name = 'produto'
	
	def get_object(self):
        obj = super().get_object()
        obj.blog_view += 1
        obj.save()
        return obj