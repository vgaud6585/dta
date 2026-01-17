from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet

# Home: List aur Create dono ke liye
def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Snippet.objects.create(title=title, content=content)
        return redirect('index')
    
    snippets = Snippet.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'snippets': snippets})

# Edit Snippet
def edit_snippet(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    if request.method == "POST":
        snippet.title = request.POST.get('title')
        snippet.content = request.POST.get('content')
        snippet.save()
        return redirect('index')
    return render(request, 'edit.html', {'snippet': snippet})

# Delete Snippet
def delete_snippet(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    snippet.delete()
    return redirect('index')
