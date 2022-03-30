from django.test import TestCase

from store.models import Category, Product

class TestCategoryModel(TestCase):
    def setUp(self):
        self.data = Category.objects.create(name='athletic', slug='athletic')
        
    def test_category_model_item(self):
        data1 = self.data
        self.assertTrue(isinstance(data1, Category))
        
    