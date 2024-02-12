import requests
from django.shortcuts import render
from django.http import JsonResponse


def check_status(request):
    url = request.POST.get('url')
    try:
        if not url:
            return JsonResponse({'status': 'No URL provided'})
        response = requests.get(url)
        status_code = response.status_code
        print(status_code)
        return JsonResponse({'status_code': status_code})
    except requests.exceptions.RequestException:
        return JsonResponse({'status_code': None})


def home(request):
    return render(request, 'home.html')
