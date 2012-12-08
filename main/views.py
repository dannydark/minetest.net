from django.template import Context, loader
from django.http import HttpResponse

def index(req):
	t = loader.get_template('main/index.html')
	c = Context({
	})
	return HttpResponse(t.render(c))

def news(req):
	t = loader.get_template('main/news.html')
	c = Context({
	})
	return HttpResponse(t.render(c))

def download(req):
	t = loader.get_template('main/download.html')
	c = Context({
	})
	return HttpResponse(t.render(c))

def contribute(req):
	t = loader.get_template('main/contribute.html')
	c = Context({
	})
	return HttpResponse(t.render(c))

