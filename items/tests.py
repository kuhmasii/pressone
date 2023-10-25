from django.test import TestCase
from django.urls import reverse

from items.models import Item


class ItemModelTestCase(TestCase):
    
    def setUp(self):
        Item.objects.create()

    def test_item_creation(self):
        """Testing an instance of a an Item Model created.
           Instance should return the primary key of the object.
        """
        ins = Item.objects.get(pk=1)

        self.assertIsInstance(ins, Item)
        self.assertTrue(ins)

    def test_data_for_instance_of_item_model(self):
        """Testing an instance data is correct
        """
        ins = Item.objects.get(pk=1)

        self.assertEqual(ins.pk, 1)

    def test_data_not_for_instance_of_item_model(self):
        """Testing an instance data is not correct
        """
        ins = Item.objects.get(pk=1)

        self.assertNotIn(ins.pk, list(range(2, 100)))

class ItemViewTestCase(TestCase):    
    
    def setUp(self):
        Item.objects.create()

    def test_get_view(self):
        """A detailed data of the API endpoint is displayed."""

        response = self.client.get(
                   reverse('items:item-detail', 
                   args=(1,),))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 1)

    
    def test_get_view_not_found(self):
        
        """Endpoint should return 404 if id is not found"""
       
        try:
            response = self.client.get(
                reverse(
                    "items:item-detail",
                    args=(999,),
                )
            )
        except:
            self.assertEqual(response.status_code, 404)
            self.assertContains(response, 'Not Found')
    
    def test_post_view(self):
        """Endpoint should return the newly created object of an Item."""

        response = self.client.post(reverse('items:item-create'))
 
        self.assertEqual(response.data.get('id'), 2)
        self.assertEqual(response.status_code, 201)
    
    # generic view test   
    def test_get_generic_view(self):
        """A detailed data of the API endpoint is displayed."""

        response = self.client.get(
                   reverse('items:item-generic-detail', 
                   args=(1,), 
               ))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 1)

    
    def test_get_generic_view_not_found(self):
        
        """Endpoint should return a 404 if id is not found"""
       
        try:
            response = self.client.get(
                reverse(
                    "items:item-generic-detail",
                    args=(999,),
                )
            )
        except:
            self.assertEqual(response.status_code, 404)
            self.assertContains(response, 'Not Found')
    
    def test_post_generic_view(self):
        """Endpoint should return the newly created object of an Item."""

        response = self.client.post(reverse('items:item-generic-create'))
 
        self.assertEqual(response.data.get('id'), 2)
        self.assertEqual(response.status_code, 201)
        

