from django.shortcuts import render,redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    posts = Post.objects.all()
    
    return render(request,'index.html',{'posts':posts})

def post(request,pk):
    post = Post.objects.get(id=pk)
    post.body = post.body.replace('\n', '<br>')
    return render(request,'post.html',{'post':post})

def add(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        user_id = request.POST['user_id']
        user = User.objects.get(id=user_id)
        name = user.username
        post = Post.objects.create(title=title, body=body,user=name)
        post.save()
        return redirect("/")
    else:
        return render(request,'add.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Credentials are not valid")
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=pass2)
                user.save()
                return redirect("login")
        else:
            messages.info(request,'Passwords are not same')
            return redirect("register")
    else:
        return render(request,'register.html')
    
def myblog(request,user_id):
    # print(user_id)
    user = User.objects.get(id=user_id)
    print(user.username)
    posts = Post.objects.filter(user=user.username)
    posts_exist = Post.objects.filter(user=user.username).exists()
    print(posts)
    print(posts_exist)
    context = {
        "posts": posts, 
        "posts_exist": posts_exist,
        }
    return render(request,'myblog.html',context)

def logout(request):
    auth.logout(request)
    return redirect("/")

def delete(request,delete_post):
    post = Post.objects.get(id=delete_post)
    print(post.title)
    user = User.objects.get(username=post.user)
    print(user.username)
    post.delete()
    return redirect("/")




