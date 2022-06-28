# from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
# from .forms import BlogForm

# Create your views here.


# def blog(request):
#     blogs = Post.objects.all()
#     context = {"blogs": blogs}
#     return render(request, 'blog.html', context)


# def add_blog(request):
#     form = BlogForm()
#     context = {"form": form}
#     if request.method == 'POST':
#         blog_form = BlogForm(request.POST)
#         if blog_form.is_valid():
#             blog_form.save()
#             return redirect("blogs")
#         else:
#             context = {'form': blog_form}
#             return render(request, 'add_form.html', context)
#     return redirect(request, 'add_form.html', context)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'