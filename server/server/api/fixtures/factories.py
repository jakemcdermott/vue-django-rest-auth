import datetime
from random import randint

from django.conf import settings
from django.contrib.auth import get_user_model
from factory import (
    LazyAttribute,
    LazyFunction,
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory
from faker import Faker

from server.api.models import (
    Post,
)


delta = datetime.timedelta
now = datetime.datetime.now

fake = Faker()


class UserFactory(DjangoModelFactory):

    class Meta:
        model = get_user_model()

    email = LazyAttribute(lambda o: '{username}@123.com'.format(username=o.username))
    first_name = LazyFunction(fake.first_name)
    last_name = LazyFunction(fake.last_name)
    username = Sequence(lambda n: '{}{}'.format(fake.user_name(), n))


class PostFactory(DjangoModelFactory):

    class Meta:
        model = Post

    author = SubFactory(UserFactory)

    title = LazyFunction(lambda: fake.text(randint(5, 20)))
    content = LazyFunction(lambda: fake.text(randint(20, 500)))
    created = LazyFunction(lambda: now() - delta(days=365))
    updated = LazyAttribute(lambda o: o.created + delta(days=randint(0, 365)))
