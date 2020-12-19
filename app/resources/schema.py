import graphene
from graphene_django import DjangoObjectType
from .models import ResoucesRequired
from graphql import GraphQLError
from protestId.models import Protest


class Resources(DjangoObjectType):
    class Meta:
        model = ResoucesRequired


class Query(graphene.ObjectType):
    resources = graphene.List(Resources,id=graphene.String(required=True))

    def resolve_resources(self, info,id):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        protest=Protest.objects.get(id=id)
        return ResoucesRequired.objects.filter(protest=protest).order_by("-quantity")
    

class CreateResource(graphene.Mutation):
    new = graphene.Field(Resources)

    class Arguments:              
        title = graphene.String()
        quantity = graphene.String()
        id=graphene.String()

    def mutate(self, info, title, quantity, id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        protest=Protest.objects.get(id=id)
        temp = ResoucesRequired.objects.create(title=title, quantity=quantity,protest=protest)
        temp.save()

        return CreateResource(new=temp)


class Mutation(graphene.ObjectType):
    create_resource = CreateResource.Field()