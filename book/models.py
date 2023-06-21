from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()


    def __str__(self):
        return self.first_name



class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=17)


    def __str__(self):
        return self.title



class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.book.title} BY {self.author.first_name}'



class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    star_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )


    def __str__(self):
        return f'{self.star_given} stars for {self.book.title} from {self.user.username}'






















































































