from rest_framework.decorators import api_view
from rest_framework.response import Response

ext_labels = {
  "1" : {
    "name" : "bottle",
    "price" : 15
  },
  "2" : {
    "name" : "duck",
    "price" : 10
  },
  "3" : {
    "name" : "heart",
    "price" : 5
  }
}   

@api_view(['GET'])
def getData(request):
    return Response(ext_labels)


