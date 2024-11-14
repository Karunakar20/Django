from django.shortcuts import get_object_or_404, render, redirect
from . models import Blog
from . forms import BlogEditForm
# Create your views here.

def home_page(request):
    data = Blog.objects.all()
    context = {'data':data}
    return render(request, 'app/home.html',context)

def View(request,pk):
    view = Blog.objects.get(id=pk)
    context = {'view':view}
    return render(request, 'app/view.html',context)

def Edit(request,pk):
    post = get_object_or_404(Blog,id=pk)
    if request.method == 'POST':
        form = BlogEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogEditForm(instance=post)
    return render(request, 'app/edit.html', {'form': form})


def Delete(request,pk):
    post = get_object_or_404(Blog,id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'app/delete.html', {'post': post})

def add(request):
    if request.method == 'POST':
        form = BlogEditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogEditForm()
    return render(request, 'app/add_blog.html', {'form': form})

def tech(request,val):
    data = Blog.objects.filter(tags=val)
    context = {'data':data}
    return render(request, 'app/tech.html',context)

def health(request,val):
    data = Blog.objects.filter(tags=val)
    context = {'data':data}
    return render(request, 'app/health.html',context)

def travel(request,val):
    data = Blog.objects.filter(tags=val)
    context = {'data':data}
    return render(request, 'app/travel.html',context)

def food(request,val):
    data = Blog.objects.filter(tags=val)
    context = {'data':data}
    return render(request, 'app/food.html',context)

def lifestyle(request,val):
    data = Blog.objects.filter(tags=val)
    context = {'data':data}
    return render(request, 'app/lifestyle.html',context)


def search(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        results = Blog.objects.filter(title__icontains=query) 
    return render(request, 'app/search.html', {'query': query, 'results': results})
    

