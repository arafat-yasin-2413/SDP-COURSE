from django.shortcuts import render,redirect 
from category.forms import CategoryForm

# Create your views here.
def add_category(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            cat_name = category_form.cleaned_data['category_name']
            # print(cat_name)
            category_form.save()
            return redirect('add_category')
    else:
        category_form = CategoryForm()    
    return render(request, 'add_category.html',{'form':category_form})
