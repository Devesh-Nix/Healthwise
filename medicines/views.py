from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine, MedicineOrder, MedicineOrderItem
from django.contrib import messages
from django.core.mail import send_mail

def medicine_list(request):
    query = request.GET.get('q')
    if query:
        medicines = Medicine.objects.filter(name__icontains=query)
    else:
        medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})

def add_to_cart(request, medicine_id):
    cart = request.session.get('cart', {})
    cart[str(medicine_id)] = cart.get(str(medicine_id), 0) + 1
    request.session['cart'] = cart
    messages.success(request, "Medicine added to cart.")
    return redirect('medicine_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    medicine_ids = cart.keys()
    medicines = Medicine.objects.filter(id__in=medicine_ids)

    cart_items = []
    total = 0
    for med in medicines:
        quantity = cart[str(med.id)]
        subtotal = med.price * quantity
        cart_items.append({'medicine': med, 'quantity': quantity, 'subtotal': subtotal})
        total += subtotal

    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total': total})

def place_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Cart is empty.")
        return redirect('medicine_list')

    if request.method == 'POST':
        full_name = request.POST['full_name']
        address = request.POST['address']
        phone = request.POST['phone']

        order = MedicineOrder.objects.create(full_name=full_name, address=address, phone=phone)
        send_mail(
            subject='Medicine Order Confirmation',
            message=f"Dear {order.full_name},\n\nYour medicine order has been received. We are preparing your order for delivery.\n\nThank you for choosing our service!",
            from_email='noreply@healthcareplatform.com',
            recipient_list=[request.user.email],
            fail_silently=False,
        )


        for med_id, quantity in cart.items():
            medicine = Medicine.objects.get(id=med_id)
            MedicineOrderItem.objects.create(order=order, medicine=medicine, quantity=quantity)

            # Reduce stock
            medicine.available_quantity -= quantity
            medicine.save()

        request.session['cart'] = {}
        messages.success(request, "Order placed successfully!")
        return redirect('medicine_list')

    return render(request, 'place_order.html')
