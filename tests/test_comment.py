import unittest
from app.models import Comment
# Comment = comment.Comment

class CommentTest(unittest.TestCase):
    """
        Test class to test the behaviour of the Comment class
    """
    def setUp(self):
        """
            Set up method that will run before every test
        """
        self.new_comment= Comment(1, 'Business', 'Consistency is key', 'Jane Doe')

    def test_initialization(self):
        self.assertEqual(self.new_comment.id, 1)
        self.assertEqual(self.new_comment.title, 'Business')
        self.assertEqual(self.new_comment.content, 'Consistency is key')
        self.assertEqual(self.new_comment.author, 'Jane Doe')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

