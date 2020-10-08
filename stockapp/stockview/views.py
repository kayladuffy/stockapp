from django.shortcuts import render

def home(request):
    import requests 
    import json
    #pk_ea4736199eb44c189f914c2ed20cade4
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_ea4736199eb44c189f914c2ed20cade4")
    

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})