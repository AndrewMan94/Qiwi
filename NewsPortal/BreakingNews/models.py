from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    unique = True

    def update_rating(self):
        result = 0
        user = self.id_user

        post_list = Post.objects.filter(id_author=self, type=Post.article)

        # суммарный рейтинг каждой статьи автора умножается на 3
        post_rating_list = post_list.values("rating")
        result = 3 * (sum(item ["rating"] for item in post_rating_list))

        # суммарный рейтинг всех комментариев автора
        comment_rating_list = Comment.objects.filter(id_user=user).values("rating")
        result += sum(item ["rating"] for item in comment_rating_list)

        # суммарный рейтинг всех комментариев к статьям автора
        for post in post_list:
            comment_in_post = Comment.objects.filter(id_post=post).values("rating")
            result += sum(item ["rating"] for item in comment_in_post)

        self.rating = result
        self.save()

    def __str__(self):
        return self.id_user.username


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=128, unique=True)
    subscribers = models.ManyToManyField(User, through="CategorySubscribers")
    unique = True

    def __str__(self):
        return self.name

    @property
    def is_subscribed(self):
        return CategorySubscribers.objects.filter(id_category=self.pk).exists()


class CategorySubscribers(models.Model):
    objects = None
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unique = True


class Post(models.Model):
    objects = None
    unique = True
    article = "AR"
    news = "NW"
    POST_TYPE = [(article, 'Статья'), (news, 'Новость')]

    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=POST_TYPE, default=article)
    created = models.DateTimeField()
    id_post_category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}: {self.text[:10]}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        result = self.text [:124] + "..."
        return result

    def get_absolute_url(self):
        return f'/post_list/{self.id}'




class PostCategory(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unique = True



class Comment(models.Model):
    objects = None
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField()
    text = models.TextField()
    rating = models.IntegerField()
    unique = True

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()