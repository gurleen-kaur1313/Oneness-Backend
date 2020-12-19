import graphene
from graphene_django import DjangoObjectType
from .models import Location
from graphql import GraphQLError
from protestId.models import Protest


class Locations(DjangoObjectType):
    class Meta:
        model = Location


class Query(graphene.ObjectType):
    locations = graphene.List(Locations,id=graphene.String(required=True))

    def resolve_locations(self, info,id):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        protest=Protest.objects.get(id=id)
        return Location.objects.filter(protest=protest)
    

class AddLocation(graphene.Mutation):
    new = graphene.Field(Locations)

    class Arguments:              
        locality= graphene.String()
        city = graphene.String()
        state = graphene.String()
        id=graphene.String()

    def mutate(self, info, locality, city, state, id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        protest=Protest.objects.get(id=id)
        temp = Location.objects.create(locality=locality, city=city, state=state, protest=protest)
        temp.save()

        return AddLocation(new=temp)


class Mutation(graphene.ObjectType):
    create_location = AddLocation.Field()