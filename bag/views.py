from django.shortcuts import render


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