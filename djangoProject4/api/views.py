from django.http.response import JsonResponse

# Create your views here.

products = [
    {
        'id': i,
        'name': f'Product {i}',
        'price': i * 1000,
        'description': i,
        'count': f'Count is {i + 5}',
        'is_active': True
    }
    for i in range(1, 10)
]
categories = [
    {
        'name': f'Category {i}',
        'id': i
    }
    for i in range(1, 10)
]


def product_list(request):
    return JsonResponse(products, safe=False)


def product_detail(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product, status=200)
    return JsonResponse({'message': 'Product not found with selected ID'}, status=400)


def category_list(request):
    return JsonResponse(categories, safe=False)


def category_detail(request, category_id):
    for category in categories:
        if category['id'] == category_id:
            return JsonResponse(category, status=200)
    return JsonResponse({'message': 'category not found with selected ID'}, status=400)
