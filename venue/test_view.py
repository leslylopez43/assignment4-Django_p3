from django.test import TestCase

# Create your tests here.
class Testviews(TestCase):

    def test_get_venue_list(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, "venue/venue_list.html")
    # def test_get_add_item_page(self):
    
    # def test_get_edit_item_page(self):
    
    # def test_can_add_item(self):

    # def test_can_delete_item(self):
    
    # def test_can_toggle_item(self):
   
        

