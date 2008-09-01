from inheritance.examples.models import Post, Article, Photo, Link


tests = """
>>> Article.objects.create(title='Make a Tumblelog')
<Article: Make a Tumblelog>

>>> Photo.objects.create(title='Self Portrait', image='photos/me.jpg')
<Photo: Self Portrait>

>>> Link.objects.create(title='Django', url='http://www.djangoproject.com/')
<Link: Django>

>>> Post.objects.order_by('title')
[<Post: Django>, <Post: Make a Tumblelog>, <Post: Self Portrait>]

>>> Post.children.order_by('title')
[<Link: Django>, <Article: Make a Tumblelog>, <Photo: Self Portrait>]

"""


__test__ = {'tests': tests}
