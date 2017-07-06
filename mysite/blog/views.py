
from django.shortcuts import render
#from django.template import loader,Context
from blog.models import BlogPost
from django.shortcuts import render_to_response
#from django.http import HttpResponse

# Create your views here.
def archive(request):
    blog_list = BlogPost.objects.all()
    return render_to_response('archive.html',{'blog_list':blog_list})

  

'''
def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(
            title = request.POST.get('title'),
            body = request.POST.get('body'),
            timestamp = request.POST.get('timestamp'),
            ).save()
    return HttpResponseRedirect('/blog/')
'''
