from django.shortcuts import redirect, render
from django import forms
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import *
from .serializers import ObjSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .scrape import scrape
from .images import get_images
from django.shortcuts import render


class NewForm(forms.Form):
    url_form = forms.URLField(label="url")




@api_view(['GET'])
def restaurantinfo(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = ObjSerializer(restaurants, many=True)
        return Response(serializer.data, content_type="application/json")
  
def my_form(request):
    if request.method == 'POST':
        # Handle form submission
        url = request.POST.get('url')
        # Call the scrape function with the URL parameter
        output, output_1 = scrape(url)
        get_images(url)
        # Render the output in a separate HTML page
        return render(request, 'restaurants/output.html', {'output': output, 'output_1': output_1}) 
    else:
        # Render the form
        return render(request, 'restaurants/index.html')

#from .models import Restaurant  # Import your Restaurant model


def add_to_db(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            # Get data from the POST request
            name = request.POST.get('name')
            address = request.POST.get('address')
            phone_num = request.POST.get('phone_num')
            timings=request.POST.get('timings')
            apc=request.POST.get('apc')
            park=request.POST.get('park')
            pet=request.POST.get('pet')
            cui=request.POST.get('cui')
            pay=request.POST.get('pay')
            mi=request.POST.get('mi')
            seat=request.POST.get('seat')
            t_reserve=request.POST.get("t_reserve")

            restaurant = Restaurant(
                R_name=name,
                R_address=address,
                R_phone=phone_num,
                R_timings=timings,
                R_apc=apc,
                R_parking=park,
                R_pet=pet,
                R_cu=cui,
                R_pay=pay,
                R_more_info=mi,
                R_seat=seat,  
                R_reserve=t_reserve,
        # Set other fields here
            )
            restaurant.save()

        # Redirect to a success page or any other page as needed
            return render(request,'restaurants/success.html')
        elif action == 'ignore':
    # Handle GET requests or other cases as needed
            #return render(request, 'restaurants/index.html')
            return redirect('my_form')
    return HttpResponse("Invalid request or missing action parameter")

@csrf_exempt            
@api_view(['POST'])
def get_url(request):
    if request.method == 'POST':
        url_form = NewForm(request.data)  # Use request.data to access JSON data

        if url_form.is_valid():
            url = url_form.cleaned_data['url_form']

            try:
                data = scrape(link=url)

                if data:
                    r = Restaurant(R_name=data[0], R_address=data[1], R_phone=data[2], R_timings=data[3],R_apc=data[4],R_parking=data[5],R_pet=data[6],R_cu=data[7],R_pay=data[8],R_more_info=data[9],R_seat=data[10],R_reserve=data[11])
                    r.save()
                    res = Restaurant.objects.all()
                    serializer = ObjSerializer(res, many=True)
                    # res.delete()
                    return Response(serializer.data, content_type="application/json")
                else:
                    return Response({"error": "Scraping failed."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(url_form.errors, status=status.HTTP_400_BAD_REQUEST)  # Bad request if form is not valid

    # Return a response in case the request method is not 'POST'
    return Response({"error": "Only POST requests are allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)