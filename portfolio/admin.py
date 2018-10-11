from django.contrib import admin
from .models import FlooringPic, ShowerPic, KitchenPic, BathtubPic, FireplacePic, CountertopPic

# Register your models here.

admin.site.register(FlooringPic)
admin.site.register(ShowerPic)
admin.site.register(KitchenPic)

admin.site.register(FireplacePic)
admin.site.register(CountertopPic)

class BathtubPicAdmin(admin.ModelAdmin):
    list_display = ('bathtub',)

admin.site.register(BathtubPic, BathtubPicAdmin)