from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateField(auto_now=True)  # 表示将评论的当前时间保存到数据库

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]

### 关于 self.text[:20]语法和字符串截取的语法一样。用demo来演示

### >>> str = '0123456789'
### >>> print (str[0:3])
### 012
### >>> print (str[:3])
### 012
### >>>

