from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

posts =[ {
    'author':'henry',
    'title':'Transport Series',
    'content':'Best containers for shipping',
    'date_posted':'11th Jan, 2023',

},
{
    'author':'Jerry',
    'title':'Logistics Series',
    'content':'Tech events happening 2023',
    'date_posted':'11th Feb, 2023',

}
]
    


def home (request):
    context ={'posts':posts}
    return render (request , 'blog/home.html',context)
def about (request):
    return render (request , 'blog/about.html',{'title':"About Us"})

def contact (request):
    return render (request , 'blog/contact.html',{'title':"Conact Us"})