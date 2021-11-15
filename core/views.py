from django.shortcuts import render
from frontend.models import Produto


def home(request):

	context = {
		'products':Produto.objects.all() if len(Produto.objects.all()) > 10 else Produto.objects.all()
	}
	return render(request, 'home.html', context)