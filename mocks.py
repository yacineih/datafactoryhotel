from flask import abort
class Post():
	POSTS=[{'id':1, 'title':'first Post', 'content': 'this is my first post'}
,{'id':2, 'title':'Second Post', 'content': 'this is my second post'}
,{'id':3, 'title':'Third Post', 'content': 'this is my third post'}

	]
	@classmethod
	def all(cls):
		"fetch all posts "
		return cls.POSTS
	@classmethod
	def find(cls,id):
		"fetch only one post"
		try:
			return cls.POSTS[id-1]
		except IndexError:
	 		abort(404)