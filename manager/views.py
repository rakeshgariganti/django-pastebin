from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import PasteForm
from models import Paste
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = PasteForm(request.POST)
		if form.is_valid:
			form.save()
			form = PasteForm()
	else:
		form = PasteForm()

	pastes = Paste.objects.all()
	paginator = Paginator(pastes,15)
	page = request.GET.get('page')
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)
	return render(request,'base.html',{'form':form, 'data':data})

def get(request,id):
	paste = get_object_or_404(Paste, pk = id)
	return render(request,'get.html',{'paste':paste})