from django.shortcuts import redirect, render


# Create your views here.
def view_bag(request):
    '''
    Renders the shopping cart page

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response representing the shopping cart page.
    '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''Add the quantity of a product to shopping bag

    Args:
        request: HTTP request
        item_id: id of the item
    '''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)