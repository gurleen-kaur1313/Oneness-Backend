import graphene
from graphene_django import DjangoObjectType
from .models import User
from graphql import GraphQLError


class Users(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    me = graphene.Field(Users)


    def resolve_me(self,info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return Blog.objects.all()

        