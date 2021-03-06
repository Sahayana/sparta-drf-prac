from django.db import models

from user.models import UserProfile, User

# Create your models here.

class BaseModel(models.Model):
    created_at  =   models.DateTimeField(auto_now_add=True, verbose_name="작성시간")
    modified_at =   models.DateTimeField(auto_now=True, verbose_name="수정시간")    

    class Meta:
        abstract = True    


class Category(BaseModel):
    
    name        =   models.CharField(max_length=50, verbose_name="카테고리명")
    description =   models.CharField(max_length=300, verbose_name="카테고리설명", blank=True)

    def __str__(self) -> str:
        return self.name


class Article(BaseModel):
    category    =   models.ManyToManyField(Category)
    author      =   models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    title       =   models.CharField(max_length=300, verbose_name="제목")
    content     =   models.TextField(verbose_name="내용")

    def __str__(self) -> str:
        return self.title


class Comment(BaseModel):
    author      =   models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    article     =   models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="글")
    content     =   models.CharField(max_length=500, verbose_name="댓글내용")
