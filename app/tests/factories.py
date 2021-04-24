import factory

from app.models import Character, Quote, Favourite


class CharacterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'app.Character'

    _id = factory.Sequence(lambda n: 'id-{}'.format(n))
    height = factory.Sequence(lambda n: 'height-{}'.format(n))   
    race = factory.Sequence(lambda n: 'race-{}'.format(n))
    gender = factory.Sequence(lambda n: 'gender-{}'.format(n))
    birth = factory.Sequence(lambda n: 'birth-{}'.format(n))
    spouse = factory.Sequence(lambda n: 'spouse-{}'.format(n))
    death = factory.Sequence(lambda n: 'death-{}'.format(n))
    realm = factory.Sequence(lambda n: 'realm-{}'.format(n))
    hair = factory.Sequence(lambda n: 'hair-{}'.format(n))
    name = factory.Sequence(lambda n: 'name-{}'.format(n))
    wikiUrl = factory.Sequence(lambda n: 'https://example.com/{}/'.format(n))


class QuoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'app.Quote'
    _id = factory.Sequence(lambda n: 'id-{}'.format(n))
    dialog = factory.Sequence(lambda n: 'dialog-{}'.format(n))
    movie = factory.Sequence(lambda n: 'movie-{}'.format(n))
    character = factory.Sequence(lambda n: 'character-{}'.format(n))


class FactoriteFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory('users.tests.factories.UserFactory')
    characters = factory.RelatedFactory(CharacterFactory)
    quotes = factory.RelatedFactory(QuoteFactory)
