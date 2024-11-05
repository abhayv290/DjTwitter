from django.shortcuts import render ,get_object_or_404 ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from .models import Tweet 
from .forms import TweetForm
from .forms import RegistrationForm


def tweet_list(req):
    tweets=Tweet.objects.all()
    return render(req, 'tweet/tweetlist.html',{'tweets':tweets})

#Creatiing the views for handling the post request ( adding the tweet )
@login_required
def tweet_create(req):
    form=None
    if req.method=='POST':
        form=TweetForm(req.POST,req.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user=req.user
            tweet.save()

            return redirect('tweet_list')
    else:
        form=TweetForm()
    return render(req, 'tweet/tweetform.html',{'form':form})


#Editing the Tweets 
@login_required
def tweetEdit(req,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=req.user)
    if req.method=='POST' :
        form=TweetForm(req.POST,req.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=req.user 
            tweet.save()
            return redirect('tweet_list')
          
    else:
        form=TweetForm(instance=tweet)
        return render(req, 'tweet/tweetform.html',{'form':form})

#This View function handles the tweet Deletion
@login_required
def tweetDelete(req,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=req.user)
    if req.method =='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(req, 'tweet/tweetdelete.html', {'tweet':tweet})
    



# This View handle the user login
def register(req):
    form=None
    if req.method=='POST':
        form=RegistrationForm(req.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(req,user)
            return redirect('tweet_list')            
    else: 
        form=RegistrationForm()
    return render(req,'registration/register.html',{'form':form})
