from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    get_object_or_404,
    CreateAPIView,
    RetrieveAPIView
)

from items.models import Item
from items.serializers import ItemSerializer


# First enhancement Approach      

class ItemAPI(APIView):
    """
    API view for handling Item objects, supporting both retrieval and creation.

    - `GET`: Retrieve an Item by its ID.
    - `POST`: Create a new Item.
    """

    def get(self, request, item_id=None):
        """
        Retrieve an Item by its ID.

        Args:
        - `request` (Request): The HTTP GET request.
        - `item_id` (int, optional): The ID of the Item to retrieve.

        Returns:
        - Response: The serialized data of the retrieved Item.
        """
        # The Problematic API was not handling errors, which could cause /
        # a break in the software product. 
        
        # using rest_framework built-in get_object_or_404 to handle errors
        
        item = get_object_or_404(Item, id=item_id)
        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new Item.

        Args:
        - `request` (Request): The HTTP POST request containing data for creating a new Item.

        Returns:
        - Response: The serialized data of the created Item, or errors if the data is invalid.
        """
        serializer = ItemSerializer(data=request.data)
        # The Problematic API did not validate the incoming request data /
        # this would save invalidated date in the db. 
        # is_valid() needs to be called before the save() method / 
        # if not, this would cause an error and a break in the product.
        
        # using is_valid function to check the validity of the data /
        # before saving it in the data base
        
        if serializer.is_valid():
            serializer.save()
            # The Problematic API was only responding with status code
            
            # included the response data  of the Item instance             
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # The Response returning error in the Problematic API \
        # wasn't checked and it was also written on the wrong line.
        
        # included the error Response check and / 
        # placed the Response on the right line.                          
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Second enhancement Approach.

# This approach would be depended on the logic of my application.
# Since my application relates with my model and it's straight forward /
# concerete generic view suits it.

class ItemCreateAPIView(CreateAPIView):
    
    """API view for creating new Item object"""
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveAPIView(RetrieveAPIView):
    
    """API view for retrieving a single Item object by its ID."""
    
    queryset = Item.objects.all()
    lookup_field = 'id'
    serializer_class = ItemSerializer


# apiview
item_api = ItemAPI.as_view()

# generic views
item_create   = ItemCreateAPIView.as_view()
item_retrieve = ItemRetrieveAPIView.as_view()
        