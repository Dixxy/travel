from django.db import models


class PostModel(models.Model):
    object = None
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to='posts')
    banner = models.ImageField(upload_to='post banners')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class NewModel(models.Model):
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'


class CommentModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='phone')
    comment = models.TextField(verbose_name='comment')

    post = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='post'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
