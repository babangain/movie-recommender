from django.shortcuts import render
from gensim.models.doc2vec import Doc2Vec
from sys import argv
from django.http import HttpResponse, JsonResponse
model = Doc2Vec.load("doc2vec_Movie_recommender_vec_150_window_10_mc_2_epochs_50.model")


def index(request):
    if request.method == 'GET':

        # sentence is the query we want to get the prediction for
        #params =  request.POST.get('input_image')

        # predict method used to get the prediction 

        # returning JSON response
        
        query =  request.GET['name']
        number = 10
        try:
        	number = int(request.GET['number'])
        except:
        	pass
        response = ""
        try:
            lst = model.docvecs.most_similar(query,topn=number)
            for i in range(len(lst)):
                response = response + lst[i][0] + "<br>"
        except :
            return HttpResponse("Some Error Occured!!! Please enter movie name correctly and ensure they name is exactly same as in the database")
        return HttpResponse(response)
# Create your views here.
