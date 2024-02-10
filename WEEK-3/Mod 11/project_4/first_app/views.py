from django.shortcuts import render

# Create your views here.
def index(request):
    data = [
  {
    "userId": 1,
    "id": 1,
    "title": "are or do repels provide blacked out except option criticizes",
    "body": "because he also accepts\nundertakes the consequences of refusal and when\nhe criticizes the trouble so that the whole\nof our things are but they are the matter will happen to the architect"
  },
  {
    "userId": 12,
    "id": 2,
    "title": "who is being",
    "body": "it is in the time of life that things should be followed; no pain will blame the blessed ones; nor will they flee from the flattery of the pleasure; nor will there be any trouble to reject them; we shall not be open to them; we shall not be able to do so, but there is nothing."
  },
  
  {
    "userId": 123,
    "id": 4,
    "title": "and he is blinded",
    "body": "by rejecting any and often to gain pleasure\nbut it is easy to assume the fault of things\nwhoever does not know the benefits here is bound by the thing and the pain itself by right\nwhosoever wants the pleasure of things"
  },
  {
    "userId": 1,
    "id": 5,
    "title": "they don't know what they hate",
    "body": "Let him seek forgiveness for repudiation, but there are other things, or let him flee, but it is, but there is pleasure, we can all be pleasures; there is no pain, nor is it held"
  },
  
  {
    "userId": 1,
    "id": 7,
    "title": "but the great easy",
    "body": "may it please some with pain that the things of life\nfor the great who are the ones who are whom no one or often\nwill repulse them because\nthey are to follow them but those which"
  }
  
]  
    return render (request,'index.html',{'data':data})


def about(request):
    print(request.GET)
    return render(request,'index.html',{'id': request.GET})