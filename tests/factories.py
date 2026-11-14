import factory
from django.contrib.auth.models import User

from book.models import Book


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "x"
    password = "test"
    is_superuser = True
    is_staff = True


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = "x"
    author = "x"
    slug = "x"
    description = "x"
    status = "want to read"
    created_by = factory.SubFactory(UserFactory)
    updated_by = factory.SubFactory(UserFactory)
