import unittest
from google.appengine.api.users import User
from test_example.simple_model import SimpleModel

class TestSimpleModel(unittest.TestCase):
  def test_creation(self):
    user = User(email = "test@foo.com")
    model = SimpleModel(goo_user = user)
    model.put()
    fetched_model = SimpleModel.all().filter('goo_user =', user).fetch(1)[0]
    self.assertEquals(fetched_model.goo_user, user)
