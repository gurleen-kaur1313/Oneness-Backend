import graphene
from graphene_django import DjangoObjectType
from .models import User
from graphql import GraphQLError


class Users(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    me = graphene.Field(Users)

    def resolve_me(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return active


class CreateUser(graphene.Mutation):
    user = graphene.Field(Users)

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        name = graphene.String()

    def mutate(self, info, **kwargs):
        nuser = User(email=kwargs.get("email"), name=kwargs.get("name"))
        nuser.set_password(kwargs.get("password"))
        nuser.save()

        return CreateUser(user=nuser)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()