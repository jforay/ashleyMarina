from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import CategoryForm, PostForm, OwnersSignupForm
from .models import Category, Post

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


def owners_signup(request):
    if request.user.is_authenticated:
        return redirect("owners")

    if request.method == "POST":
        form = OwnersSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            send_mail(
                subject='New Account Request - Harborage at Ashley Marina',
                message=(
                    f'A new account request was submitted:\n\n'
                    f'Name: {user.first_name} {user.last_name}\n'
                    f'Username: {user.username}\n'
                    f'Email: {user.email}\n\n'
                    f'Log in as admin and visit /owners/pending-approvals/ to approve or deny.'
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.SITE_ADMIN_EMAIL],
                fail_silently=True,
            )

            return redirect("owners_pending")
    else:
        form = OwnersSignupForm()

    return render(request, "owners/signup.html", {"form": form})


def owners_pending(request):
    return render(request, "owners/pending.html")


@user_passes_test(lambda u: u.is_superuser)
def pending_approvals(request):
    pending_users = User.objects.filter(is_active=False).order_by('date_joined')
    return render(request, 'owners/pending_approvals.html', {'pending_users': pending_users})


@user_passes_test(lambda u: u.is_superuser)
def approve_user(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=pk)
        user.is_active = True
        user.save()
        send_mail(
            subject='Your Harborage at Ashley Marina account has been approved',
            message=(
                f'Hi {user.first_name},\n\n'
                f'Your account has been approved. You can now log in at:\n'
                f'https://harborageatashleymarina.com/accounts/login/\n\n'
                f'Username: {user.username}'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=True,
        )
    return redirect('pending_approvals')


@user_passes_test(lambda u: u.is_superuser)
def deny_user(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=pk)
        user.delete()
    return redirect('pending_approvals')
