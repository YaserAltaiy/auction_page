from unicodedata import category
from django.contrib import admin
from .models import User,Auction_list,Category,bids,comment,Watch_list

# Register your models here.
admin.site.register(User)
admin.site.register(Auction_list)
admin.site.register(Category)
admin.site.register(bids)
admin.site.register(comment)
admin.site.register(Watch_list)
