from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import CategoryForm,PostForm
from .models import Category,Post
# Create your views here.
@login_required(login_url='/accounts/login/')
def owners(request):
    categories = Category.objects.all()

    return render(request, 'owners/owners_home.html',{'categories':categories})

@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.is_superuser)
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owners')
    else:
        form = CategoryForm()
    return render(request, 'owners/create_category.html', {'form': form})

@login_required(login_url='/accounts/login/')
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = category.posts.order_by('-created_at')
    return render(request, 'owners/category_detail.html', {'category': category, 'posts': posts})

@login_required(login_url='/accounts/login/')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'owners/post_detail.html', {'post': post})


@login_required(login_url='/accounts/login/')
def new_post(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category = category
            post.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = PostForm()
    return render(request, 'owners/new_post.html', {'form': form, 'category': category})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_superuser:
        return redirect('post_detail', pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', pk=pk)
    return render(request, 'owners/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_superuser:
        return redirect('post_detail', pk=pk)
    if request.method == 'POST':
        category_pk = post.category.pk
        post.delete()
        return redirect('category_detail', pk=category_pk)
    return render(request, 'owners/confirm_delete.html', {'object': post, 'type': 'Post'})


@user_passes_test(lambda u: u.is_superuser)
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owners')
    else:
        form = CategoryForm()
    return render(request, 'owners/create_category.html', {'form': form})



@user_passes_test(lambda u: u.is_superuser)
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('owners')
    return render(request, 'owners/edit_category.html', {'form': form, 'category': category})



@user_passes_test(lambda u: u.is_superuser)
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('owners')
    return render(request, 'owners/confirm_delete.html', {'object': category, 'type': 'Category'})