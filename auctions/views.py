from asyncio.windows_events import NULL
from datetime import datetime
from lib2to3.pgen2.token import GREATER
from queue import Empty
from time import timezone
from tkinter import IntVar
from turtle import title
from unicodedata import category
# from xml.dom.minidom import Comment
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib import messages

from .models import Auction_list, Category, User, bids, comment, Watch_list


def index(request):
    auctions = []
    auctions = Auction_list.objects.filter(auction_status=1)
    lists = []
    for i in reversed(auctions):
        lists.append(i)
    return render(request, "auctions/index.html",{
        "lists" : lists,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    categories = []
    categories = Category.objects.all()
    return render(request,"auctions/create.html",{
        "categories" : categories,
    })

def saving(request):
    if request.method == "POST":
        
        Lc = request.POST.get("option")
        Lca = Category.objects.get(list_category = Lc)
        Lu = request.user
        content = Auction_list.objects.create(
            title=request.POST.get("Ltitle"),
            description=request.POST.get("Ldesc"),
            start_bid=request.POST.get("Lstartingbid"),
            image=request.POST.get("Limageurl"),
            auction_status=1,
            time_create=datetime.datetime.now(),
            creator_id=Lu,
            category_list=Lca,
            )
        thisid = content.pk
        return listing(request,thisid)
    else:
        return render(request, "auctions/create.html")


def listing(request,thisid):
    test = Watch_list.objects.filter(user = request.user, item = thisid)
    list = Auction_list.objects.get(id = thisid)
    comm = []
    comm = comment.objects.filter(items = thisid)
    winner = None
    lastbid = bids.objects.filter(item = list.id).last()
    if lastbid is None:
        lastbid = 0
    else:
        winner = lastbid.user_bid
    
    if comm is NULL:
        return render(request, "auctions/listing.html", {
            "list" : list,
            "test" : test,
            "winner" : winner,
        })
    else:
        return render(request, "auctions/listing.html", {
            "list" : list,
            "listcomment" : comm,
            "test" : test,
            "winner" : winner,
        })
    
    
def biding(request,thisid):
    list = Auction_list.objects.get(id = thisid)
    new =int(request.POST["newbid"])
    oldbid = list.start_bid
    Lu = request.user
    if new > oldbid :
        content = bids.objects.create(
            item = list,
            value = new,
            user_bid = Lu,
            user_time_bid = datetime.datetime.now(),
        )
        list.start_bid = new
        list.save(update_fields=['start_bid'])
    return listing(request,thisid)
    
def commenting(request,thisid):
    list = Auction_list.objects.get(id = thisid)
    newcomment = request.POST["newcomment"]
    Lu = request.user
    contents = comment.objects.create(
        items = list,
        content = newcomment,
        comment_time = datetime.datetime.now(),
        user_comment = Lu,
    )
    return listing(request,thisid)

def showcomment(request,thisid):
    comm = []
    comm = comment.objects.get(items = thisid)
    listcomment = []
    if comm is Empty:
        return listing(request,thisid)
    else:
        for i in reversed(comm):
            listcomment.append(i)


def watchlist(request):
    user1 = request.user.id
    auctions = []
    auctions = Watch_list.objects.filter(user = user1)
    item = []
    for y in auctions:
        yyy = y.item
        item.append(yyy)
    return render(request, "auctions/watchlist.html",{
        "lists" : item,
    })


def watchcreate(request,thisid):
    us = request.user
    list = Auction_list.objects.get(id = thisid)
    content = Watch_list.objects.create(
        item = list,
        user = us,
    )
    return listing(request,thisid)


def watchdelete(request,thisid):
    us = request.user
    list = Auction_list.objects.get(id = thisid)
    watch = Watch_list.objects.get(user=us, item=list)
    watch.delete()
    return listing(request,thisid)


def cate(request):
    categories = []
    categories = Category.objects.all()
    selected = request.POST.get("option")
    if selected is None:
        
        return render(request,"auctions/category.html",{
            "categories" : categories,
        })
    else:
        se = Category.objects.get(list_category=selected)
        sel = se.id
        auctions = Auction_list.objects.filter(category_list = sel)
        return render(request,"auctions/category.html",{
            "categories" : categories,
            "auctions" : auctions,
        })


def close(request,thisid):
    thislist = Auction_list.objects.get(id=thisid)
    thislist.auction_status = 0
    thislist.save(update_fields=['auction_status'])
    return listing(request,thisid)