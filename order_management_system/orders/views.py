from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import CustomerForm 

def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            # Send confirmation email
            send_mail(
                'Welcome to Our Order Management System',
                f'Hello {customer.name},\n\nThank you for registering with us.',
                'from@example.com',
                [customer.email],
                fail_silently=False,
            )
            return redirect('success')
    else:
        form = CustomerForm()
    return render(request, 'orders/register.html', {'form': form})

def success(request):
    return render(request, 'orders/success.html')
# from django.shortcuts import render, redirect
# from .forms import CustomerForm

# def register_customer(request):
#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             customer = form.save()
#             return redirect('success')
#     else:
#         form = CustomerForm()
#     return render(request, 'orders/register.html', {'form': form})
