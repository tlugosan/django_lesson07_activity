from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post, Category 

class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)
        
    # add this test method to the PostTestCase
    def test_string_representation_post(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
        
    # add this test method to the CategoryTestCase
    def test_string_representation_category(self):
        expected = "This is a category name"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)
