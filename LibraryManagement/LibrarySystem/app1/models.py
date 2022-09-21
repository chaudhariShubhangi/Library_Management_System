from django.core.validators import RegexValidator
from django.db import models


class Role(models.Model):
    """RoleList model."""

    role_name = models.CharField(max_length=222, blank=True, null=True, unique=True)

    class Meta:
        """Meta."""

        managed = True
        db_table = "role_list"
        ordering = ["pk"]

    def _str_(self):
        """_str_."""
        return self.role_name

class User(models.Model):
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField (max_length=30,blank=True)
    user_name = models.CharField (max_length=30)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number format: '+999999999'. Up to 15 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=30)
    user_role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)

    def register(self):
        self.save()

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200,blank=True, null=True)
    category = models.CharField(max_length=50,blank=True, null=True)
    added_date = models.DateField(null=True)


    def __str__(self):
        return str(self.book_name) + " [" + str(self.author_name) + ']'

