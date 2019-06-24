from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import User, Category, Device, Brand, Purchase



def home(request):
    devices = Device.objects.all()
    context = {'devices':devices}
    return render(request, 'store/home.html', context)


def detail(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    context = {'device':device}

    if request.method == "POST":
        if request.user.is_authenticated:
            Purchase.objects.create(device=device, price=device.price, user=request.user)

            messages.success(request, f"{request.user.username} you are purchase {device.name}")
            return redirect('home')

        messages.warning(request, "you are need to login first")
        return redirect('login')

    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')

    #TODO all device must be has a quantity
    if not query:
        devices = Device.objects.all()
    else:
        devices = Device.objects.filter(name__icontains=query)

    if not devices.exists():
        devices = Device.objects.filter(brand__name__icontains=query)

    if not devices.exists():
        devices = Device.objects.filter(category__name__icontains=query)
    
    context = {'devices': devices, }
    return render(request, 'store/home.html', context)

@login_required
def cart(request):
    purchases = request.user.purchases.all()
    context = {'purchases':purchases}
    return render(request, 'store/cart.html', context)