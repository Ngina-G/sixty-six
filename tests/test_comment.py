import unittest
from app.models import User, Comment
from app import db

class CommentTest(unittest.TestCase):
    """
        Test class to test the behaviour of the Comment class
    """
    def setUp(self):
        """
            Set up method that will run before every test
        """
        self.user_Jane = User(username = 'Jane',password = 'potato', email = 'jane@ms.com')
        self.new_comment= Comment(pitch_id=1, content='Consistency is key', author='Jane Doe', user=self.user_Jane)

    def test_initialization(self):
        self.assertEquals(self.new_comment.pitch_id, 1)
        self.assertEquals(self.new_comment.content, 'Consistency is key')
        self.assertEquals(self.new_comment.author, 'Jane Doe')
        self.assertEquals(self.new_comment.user, self.user_Jane)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(1)
        self.assertTrue(len(got_comments) == 1)