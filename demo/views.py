from django.shortcuts import render

# Create your views here.

def aboutus(request):
	return render(request,"about-us.html")


def index(request):
	return render(request,"index.html")

def purposes(request):
	return render(request,"purposes.html")

def showcase(request):
	return render(request,"showcase.html")

def singlepost(request):
	return render(request,"single-post.html")

def singleproduct(request):
	return render(request,"single-product.html")

def singlepurpose(request):
	return render(request,"single-purpose.html")

def storecatalog(request):
	return render(request,"store-catalog.html")

def termsofuse(request):
	return render(request,"terms-of-use.html")

def privacypolicy(request):
	return render(request,"privacy-policy.html")

def pricing(request):
	return render(request,"pricing.html")

def gridblog(request):
	return render(request,"grid-blog.html")

def gallery(request):
	return render(request,"gallery.html")

def faqs(request):
	return render(request,"faqs.html")

def contacts(request):
	return render(request,"contacts.html")

def cart(request):
	return render(request,"cart.html")

def bookanappointment(request):
	return render(request,"book-an-appointment.html")

def p404page(request):
	return render(request,"404-page.html")
