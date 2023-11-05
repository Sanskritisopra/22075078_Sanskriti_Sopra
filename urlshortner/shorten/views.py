from django.shortcuts import render,redirect
import random
import string
from .models import Url
from .forms import Urldata

def uniqueShortCode(length=10):
    chars = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(chars) for x in range(length))

        if not Url.objects.filter(short_url=short_code).exists():
            return short_code

def shorten_url(request):
    if request.method == 'POST':
        form = Urldata(request.POST)
        if form.is_valid():
            # Generate a unique short URL code
            short_url = uniqueShortCode()
            url = form.cleaned_data["url"]
            new_url = Url(long_url=url,short_url=short_url)
            new_url.save()
            return redirect("/")
    else:
        form = Urldata()
        
    data = Url.objects.all()
    context={"form":form,"data":data}
    return render(request, 'index.html',context)

def urlredirect(request,short_url):
    data = Url.objects.get(short_url=short_url)
    return redirect(data.long_url)