from django.db import models

class User_id(models.Model) :
    name = models.IntegerField(null=True)

    def __str__(self) :
        return self.name

class Comment_id(models.Model) :
    name = models.IntegerField(null=True)

    def __str__(self) :
        return self.name
class Comment_id(models.Model) :
    name = models.IntegerField(null=True)

    def __str__(self) :
        return self.name

class tag (models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.namee

class Score(models.Model) :
    name = models.IntegerField(null=True)

    def __str__(self) :
        return self.name



class Site(models.Model):
    user_id = models.IntegerField(null=True)
    comment_id = models.IntegerField(null=True)
    post_id = models.IntegerField(null=True)
    score = models.IntegerField(null=True)
    tag = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
