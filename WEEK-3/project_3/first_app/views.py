from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author': 'Rahim', 'age':8, 'lst': ['python','is','best '], 'courses': [
        {
            'id': 1,
            'name': 'Python',
            'fee': 5000
        },
        
        {
            'id': 2,
            'name': 'Django',
            'fee': 10000
        },

        {
            'id': 3,
            'name': 'C++',
            'fee': 1000
        },
    ],
    
    'birthday' : datetime.datetime.now(),
    'val': ' ',
    
    } 
    return render(request,'first_app/home.html',context=d)