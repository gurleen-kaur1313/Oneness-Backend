import graphene
from graphene_django import DjangoObjectType
from .models import Emergency
from graphql import GraphQLError


class Emergencies(DjangoObjectType):
    class Meta:
        model = Emergency


class Query(graphene.ObjectType):
    myemergency = graphene.List(Emergencies)


    def resolve_myemergency(self,info):
        active=info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Emergency.objects.all().order_by("-time")


class AddEmergency(graphene.Mutation):
    myEmergency = graphene.Field(Emergencies)

    class Arguments:
        longitude = graphene.String()
        latitude = graphene.String()
        date = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user
        test = Emergency.objects.create(user=user)
        test.longitude = kwargs.get("longitude")
        test.latitude = kwargs.get("latitude")
        test.date = kwargs.get("date")
        test.save()
        return AddEmergency(myEmergency=test)

class Mutation(graphene.ObjectType):
    add_emergency = AddEmergency.Field()

