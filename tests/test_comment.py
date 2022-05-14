import unittest
from app.models import Comment,Pitch
from app import db

class CommentTest(unittest.TestCase):
    """
        Test class to test the behaviour of the Comment class
    """
    def setUp(self):
        """
            Set up method that will run before every test
        """
        self.new_comment= Comment('Consistency is key','Jane Doe')

    def test_initialization(self):
        self.assertEquals(self.new_comment.content, 'Consistency is key')
        self.assertEquals(self.new_comment.author, 'Jane Doe')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


    def test_get_comments_by_pitch_id(self):

        got_comments = Comment.get_comments(1)
        self.assertFalse(len(got_comments) >= 1)
