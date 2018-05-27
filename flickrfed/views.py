import flickrapi
import requests
import json
from django.shortcuts import render
from PIL import Image
from django.http import HttpResponse, JsonResponse 

#homepage
def home(request):
	return render(request, 'flickrfed/home.html')

#about page
def aboutUs(request):
	return render(request, 'flickrfed/aboutus.html')

#contact page
def contactUs(request):
	return render(request, 'flickrfed/contactus.html')

#search images page
def searchImages(request):
	return render(request, 'flickrfed/images.html')

#view all images page
def allImages(request):
	return render(request, 'flickrfed/allimages.html')

#fetch images from flickr api and display
def getImages(request):
	reqimages = requests.get("https://api.flickr.com/services/rest/?method=flickr.people.getPublicPhotos&api_key=a5e95177da353f58113fd60296e1d250&user_id=24662369@N07&format=json&nojsoncallback=1")
	images = json.loads(reqimages.content)

	photolen = len(images['photos']['photo'])

	keyword = str(request.GET.keys()[0].strip('"'))

	imgdetails = []
	for i in range(0, photolen):
		try:
			if keyword.lower() in images['photos']['photo'][i]['title'].lower():
				imgObj = images['photos']['photo'][i]
				urlDefault = 'https://farm' + str(imgObj['farm']) + '.staticflickr.com/' + str(imgObj['server']) + '/' + str(imgObj['id']) + '_' + str(imgObj['secret']) + '.jpg'
				desc = []
				desc.append(urlDefault)
				desc.append(images['photos']['photo'][i]['title'])
				imgdetails.append(desc)
		except:
			continue

	responseJSON = json.dumps(imgdetails)
	return HttpResponse(responseJSON, content_type = "application/json")	