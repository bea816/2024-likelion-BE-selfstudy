from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile

"""
Post 모델 필드가 User 필드 참조 Post -> User
Post -> User 접근 가능 ex) post.author.username
User 모델에서 Post 참조하지 않음 그래서 User -> Post 참조 X
ex) user.post.title >> error

author 필드에서 related_name인 posts는
view에서 역참조할 때 쓰임
user = User.objects.get(pk=1)
posts = user.post_set.all()
또는 
user = User.objects.get(pk=1)
posts = user.posts.all()
"""

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.jpg')
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)
    published_date = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()