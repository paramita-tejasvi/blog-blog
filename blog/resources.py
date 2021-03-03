from tastypie.resources import ModelResource
from blog.models import Post, Comment
from tastypie.authorization import Authorization


class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization = Authorization()
        fields = ['id', 'title', 'text', 'author']


class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        fields = ['post', 'author', 'text']