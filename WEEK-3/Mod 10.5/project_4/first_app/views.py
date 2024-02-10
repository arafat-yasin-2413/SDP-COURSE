from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {
        'lst':['Python','is','fun','to','me'],
        'birthday': datetime.datetime.now(),
        'text1':"",
        'word1':"you",

        'lst2':[
            
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
            {'name': 'Peter', 'age': 17},
        ],

        'text2': 'This is my text',






        








    }
    return render (request,'first_app/home.html',d)

