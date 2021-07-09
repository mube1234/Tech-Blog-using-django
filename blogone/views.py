from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from blogone.forms import *;
from blogone.models import Post, Comment
from django.db.models import Q

def post_listing(request):
    tech_list = Post.objects.filter(category='Technology').order_by('-date_created')
    comsec_list = Post.objects.filter(category='Computer_Security').order_by('-date_created')
    tips_list = Post.objects.filter(category='Tips_and_Trick').order_by('-date_created')
    recent_post = Post.objects.all().order_by('-date_created')

    paginator1 = Paginator(tech_list, 3) # Show 3 posts per page
    paginator2 = Paginator(comsec_list, 2)
    paginator3 = Paginator(tips_list, 4)
    paginator4 = Paginator(recent_post, 3)

    page = request.GET.get('page')

    post = paginator1.get_page(page)
    comsec_post = paginator2.get_page(page)
    tips_post = paginator3.get_page(page)
    recently_posted = paginator4.get_page(page)

    # #for ip address
    # def get_ip(request):
    #     address=request.META.get('HTTP_X_FORWARDED_FOR')
    #     if address:
    #         ip=address.split(',').[0]
    #     else:
    #         ip=request.META.get('REMOTE_ADDR')
    #     return ip
    # ip=get_ip(request)
    # u=User(user=ip)
    # result=User.objects.filter(Q(user__icontains=ip))
    # if len(result)==1:
    #     print("user exist")
    # elif len(result)>1:
    #     print("user exist more")
    # else:
    #     u.save()
    #     print("user is unique")
    # count=User.objects.all().count()
    print("total count is",count)
    context={'posts': post,
             'comsec_posts':comsec_post,
             'tips_posts':tips_post,
             'recent_posts':recently_posted,
             }
    return render(request, 'blogone/index.html',context )
class PostListView(ListView):
    model=Post
    template_name = 'blogone/index.html'
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 3

class TechPostListView(ListView):
     model = Post
     template_name = 'blogone/technology_news.html'
     context_object_name = 'teck'
     ordering = ['-date_created']
     paginate_by = 4
class ComsecPostListView(ListView):
    model = Post
    template_name = 'blogone/comsec_news.html'
    context_object_name = 'comsec'
    ordering = ['-date_created']
    paginate_by = 4

@login_required(login_url='login')
def Add_post(request):
    form=PostForm(initial={'author': request.user})
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'blogone/add_post.html',context)

def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    comments=Comment.objects.filter(post=post,reply=None).order_by('-id')
    if request.method=='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            full_name=request.POST.get('Full_Name')
            email=request.POST.get('email')
            reply_id=request.POST.get('comment_id')
            comments_qs=None
            if reply_id:
                comments_qs=Comment.objects.get(id=reply_id)
            Comment.objects.create(post=post,content=content,Full_Name=full_name,email=email,reply=comments_qs)
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form=CommentForm()


    context={'comments':comments,
             'post': post,
             'comment_form':comment_form,

             }
    return render(request,'blogone/post_detail.html',context)
def technews(request):
    tech_news=Post.objects.filter(category='Technology').order_by('-date_created')
    tech_no=tech_news.count()
    context={'tech_news':tech_news,
             'tech_no':tech_no}
    return render(request,'blogone/tecknology_news.html',context)
def tips_and_trick(request):
    tips_news=Post.objects.filter(category='Tips_and_Trick').order_by('-date_created')
    paginator = Paginator(tips_news, 6)  # Show 25 contacts per page
    tips_no=tips_news.count()
    page = request.GET.get('page')
    tipstik = paginator.get_page(page)
    context={'tips':tipstik,
             'tips_no':tips_no}
    return render(request,'blogone/tips_news.html',context)

def comsecnews(request):
    comsec_news=Post.objects.filter(category='Computer_Security').order_by('-date_created')
    comsec_no=comsec_news.count()
    context={'comsec_news':comsec_news,
             'comsec_no':comsec_no}
    return render(request,'blogone/comsec_news.html',context)
def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username or password is incorrect')

        context={}
        return render(request,'blogone/login.html',context)
@login_required(login_url='login')
def deletepost(request,id):
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('home')
@login_required(login_url='login')
def deletecomment(request,id):
    comment=get_object_or_404(Comment,id=id)
    comment.delete()
    return redirect('home')
@login_required(login_url='login')
def editpost(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method=='POST':
        form=EditPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'post updated successfully')
            return redirect(post.get_absolute_url())
    else:
        form=EditPostForm(instance=post)
    context={'form':form}
    return render(request,'blogone/editpost.html',context)

def give_suggestion(request):
    form = SuggestForm()
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'suggestion sent successfully ')
            return redirect('suggestion')
    context = {'form': form}
    return render(request, 'blogone/suggestion.html', context)
@login_required(login_url='login')
def view_suggestion(request):
    v_suggest=Suggestion.objects.all().order_by('-timestamp')
    total_suggest=v_suggest.count()
    context={'v_suggest': v_suggest,
             'total_suggest':total_suggest}
    return render(request, 'blogone/view_suggestion.html', context)
@login_required(login_url='login')
def view_viewer(request):
    viewers=User.objects.all()
    total_viewer=viewers.count()
    context={'viewers': viewers,
             'total_viewer':total_viewer}
    return render(request, 'blogone/view_viewer.html', context)
def logoutView(request):
    logout(request)
    return redirect('login')