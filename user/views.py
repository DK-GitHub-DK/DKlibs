from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from datetime import date
from django.contrib.auth.decorators import login_required
from .decorators import *
due_day = 20
user_due_day = 30
# Create your views here.
def browse(request):
    books = Books.objects.all()
    no_of_books = books.count()
    available = books.filter(Status = 'available').count()

    BookName = request.GET.get('BookName')
    AuthorName = request.GET.get('AuthorName')
    Status = request.GET.get('Status')

    Adventure = request.GET.get('Adventure')
    if Adventure == 'on':
        books = books.filter(Genre = 12)

    Comics = request.GET.get('Comics')
    if Comics == 'on':
        books = books.filter(Genre = 14)

    Mythopoeia = request.GET.get('Mythopoeia')
    if Mythopoeia == 'on':
        books = books.filter(Genre = 9)

    Horror = request.GET.get('Horror')
    if Horror == 'on':
        books = books.filter(Genre = 13)

    SpyFiction = request.GET.get('SpyFiction')
    if SpyFiction == 'on':
        books = books.filter(Genre = 11)

    Thriller = request.GET.get('Thriller')
    if Thriller == 'on':
        books = books.filter(Genre = 10)

    Mystery = request.GET.get('Mystery')
    if Mystery == 'on':
        books = books.filter(Genre = 8)

    Fantasy = request.GET.get('Fantasy')
    if Fantasy == 'on':
        books = books.filter(Genre = 7)

    if BookName != '' and BookName is not None:
        books = books.filter(BookName__icontains= BookName)

    if AuthorName != '' and AuthorName is not None:
        books = books.filter(AuthorName__icontains= AuthorName)

    if Status != '' and Status is not None:
        books = books.filter(Status = Status)

    context = {'books': books,'no_of_books': no_of_books, 'no_of_available': available, 'filter': filter}

    if request.user.is_authenticated:
        customer = request.user.customer
        product = Orders.objects.filter(Customer = customer,  Status__in = ['delivering','delivered']).count()
        context['mybooks'] = product

    return render(request, 'user/browse.html', context)

def bookinfo(request, pk):
    book = Books.objects.get(id = pk)
    context = {'book': book}
    return render(request, 'user/bookinfo.html', context)

def signup(request):
    print(request.POST)
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + username)
            group = Group.objects.get(name = 'customer')
            user.groups.add(group)
            Customer.objects.create(user = user, name = username, email = email, PhoneNo = request.POST['PhoneNo'], Address = request.POST['Address'])
            return redirect('signin')
    context = {'form':form}
    return render(request, 'user/register.html', context)

def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('browse')

        else:
            messages.info(request,  'Username/Password is incorrect')

    return render(request, 'user/signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url = 'signin')
def mybooks(request):
    pk = request.user.customer.id
    books_with_me = Orders.objects.filter(Customer = pk, Status = 'delivered')
    books_coming_to_me = Orders.objects.filter(Customer = pk, Status = 'delivering')
    today = date.today()
    for i in books_with_me:
        global due_day
        value = due_day - ((today - i.recieved_on).days)
        if value == 1:
            i.due_on = 'Tomorrow'
        elif value == 0:
            i.due_on = 'Today'
        elif value < 0:
            i.due_on = 'ITS DUE'
        else:
            i.due_on = str(value) + ' days'
    context = {'orders': books_with_me, 'incomingbooks': books_coming_to_me}
    return render(request, 'user/mybooks.html',context)

@login_required(login_url = 'signin')
def orderbook(request, pk):
    customer = request.user.customer
    product = Books.objects.get(id = pk)
    Orders.objects.create(Customer = customer, Product = product, Status = 'delivering')
    product.Status= 'unavailable'
    product.save()
    return redirect('mybooks')

@login_required(login_url = 'signin')
def returnbook(request, pk):
    order = Orders.objects.get(id = pk)
    context = {'order': order}
    return render(request, 'user/returnconfirm.html', context)

@login_required(login_url = 'signin')
def returnconfirm(request, pk):
    order = Orders.objects.get(id = pk)
    order.Status = 'returning'
    order.save()
    return redirect('mybooks')

@login_required(login_url = 'signin')
@allowed_users(allowed_roles = ['admin'])
def chores(request):
    orders = Orders.objects.filter(Status = 'delivering')
    returns = Orders.objects.filter(Status = 'returning')
    today = date.today()
    global user_due_day
    for i in orders:
        if i.Customer.DatePayed is not None:
            value = user_due_day - ((today - i.Customer.DatePayed).days)
            if value < 0:
                i.Customer.DatePayed = 'ITS DUE'
        else:
            i.Customer.DatePayed = 'ITS DUE'
    for i in returns:
        if i.Customer.DatePayed is not None:
            value = user_due_day - ((today - i.Customer.DatePayed).days)
            if value < 0:
                i.Customer.DatePayed = 'ITS DUE'
        else:
            i.Customer.DatePayed = 'ITS DUE'
    context = {'orders':orders, 'returns': returns}
    return render(request, 'user/Chores.html', context)

@login_required(login_url = 'signin')
@allowed_users(allowed_roles = ['admin'])
def userinfo(request, pk):
    customer = Customer.objects.get(id = pk)
    today = date.today()
    global user_due_day
    if customer.DatePayed is not None:
        value = user_due_day - ((today - customer.DatePayed).days)
        if value == 1:
            customer.Paydate = 'Tomorrow'
        elif value == 0:
            customer.Paydate = 'Today'
        elif value < 0:
            customer.Paydate = 'ITS DUE'
        else:
            customer.Paydate = str(value) + ' days'
    else:
        customer.Paydate = 'ITS DUE'
    context = {'user': customer}
    return render(request, 'user/userinfo.html', context)

@login_required(login_url = 'signin')
@allowed_users(allowed_roles = ['admin'])
def deliverconfirm(request, pk):
    order = Orders.objects.get(id = pk)
    context = {'order': order}
    return render(request, 'user/deliverconfirm.html', context)

@login_required(login_url = 'signin')
@allowed_users(allowed_roles = ['admin'])
def deliver(request, pk):
    today = date.today()
    order = Orders.objects.get(id = pk)
    order.Status = 'delivered'
    order.recieved_on = today
    order.save()
    return redirect('chores')

@login_required(login_url = 'signin')
@allowed_users(allowed_roles = ['admin'])
def returns(request, pk):
    today = date.today()
    order = Orders.objects.get(id = pk)
    order.returned_on = today
    book = Books.objects.get(id = order.Product.id)
    book.Status = 'available'
    order.Status = 'returned'
    order.save()
    book.save()
    return redirect('chores')

@login_required(login_url = 'signin')
def activity(request, pk):
    customer = Customer.objects.get(id = pk)
    orders = reversed(Orders.objects.filter(Customer = customer))
    context = {'orders': orders}
    return render(request, 'user/activity.html', context)

@login_required(login_url = 'signin')
@allowed_users(allowed_roles = ['admin'])
def pay(request, pk):
    today = date.today()
    user = Customer.objects.get(id = pk)
    user.DatePayed = today
    user.save()
    return redirect('chores')
