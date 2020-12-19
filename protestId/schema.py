import graphene
from graphene_django import DjangoObjectType
from .models import Protest, Calendar
from graphql import GraphQLError


class Protests(DjangoObjectType):
    class Meta:
        model = Protest


class Dates(DjangoObjectType):
    class Meta:
        model = Calendar


class Query(graphene.ObjectType):
    allprotest = graphene.List(Protests)
    oneprotest = graphene.Field(Protests, id=graphene.String(required=True))
    dates = graphene.Field(Dates)

    def resolve_allprotest(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Protest.objects.all()

    def resolve_oneprotest(self, info, id):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        protest = Protest.objects.get(id=id)
        return protest

    def resolve_dates(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Calendar.objects.all()


class CraeteProtest(graphene.Mutation):
    new = graphene.Field(Protests)

    class Arguments:              
        title = graphene.String()
        upi = graphene.String()

    def mutate(self, info, title, upi):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        temp = Protest.objects.create(title=title, upiId=upi)

        return CraeteProtest(new=temp)


class Mutation(graphene.ObjectType):
    create_protest = CraeteProtest.Field()
