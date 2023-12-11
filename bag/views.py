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
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)