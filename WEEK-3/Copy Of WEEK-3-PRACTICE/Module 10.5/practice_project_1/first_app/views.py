from django.shortcuts import render
import datetime

context = {
    'num': 21,
    'string_1': "I'am nobody",
    'name': 'rakib',
    'string_2': 'String with spaces',
    'birthday': datetime.datetime.now(),
    'empty_string':"",
    'my_dict': [
        {'name': 'Zubaida', 'age': 19},
        {'name': 'Alamin', 'age': 22},
        {'name': 'Jalal', 'age': 31},
                ],

    'file_sz': 123456432233,
    'my_list': [20,30,10],
    'my_list_2':[7,8,9],
    'string_3': ['Python', 'is', 'fun', 'and', 'love'],
    'name_2': 'Rayhan',

    'blog_date' : datetime.datetime(2024, 2, 4, 16, 10),
    'comment_date': datetime.datetime(2024, 2, 4, 22, 0),


    
    }


# Create your views here.
def home(request):
    return render(request,'first_app/home.html',context)