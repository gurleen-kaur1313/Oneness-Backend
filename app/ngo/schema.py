import graphene
from graphene_django import DjangoObjectType
from .models import NGO
from graphql import GraphQLError


class ngos(DjangoObjectType):
    class Meta:
        model = NGO


class Query(graphene.ObjectType):
    getngo = graphene.List(ngos)


    def resolve_getngo(self,info):
        return NGO.objects.all().order_by("-name")


class AddNgo(graphene.Mutation):
    info = graphene.Field(ngos)

    class Arguments:
        name = graphene.String()
        ngo_id = graphene.String()


    def mutate(self, info, **kwargs):
        ngo=NGO.objects.create()
        ngo.name = kwargs.get("name")
        ngo.ngo_id = kwargs.get("ngo_id")

        ngo.save()

        return AddNgo(info=ngo)


class Mutation(graphene.ObjectType):
    add_ngo = AddNgo.Field()
