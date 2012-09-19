"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#from views import unfollow
#from django.contrib.auth.models import User
#
#l = User.objects.all()
#a = l[4]
#b = l[1]
#unfollow(a, b)
#print "Done"
