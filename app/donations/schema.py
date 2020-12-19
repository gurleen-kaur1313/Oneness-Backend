import graphene
from graphene_django import DjangoObjectType
from .models import Donation
from graphql import GraphQLError
from protestId.models import Protest


class Donations(DjangoObjectType):
    class Meta:
        model = Donation


class Query(graphene.ObjectType):
    donations = graphene.List(Donations,id=graphene.String(required=True))

    def resolve_donations(self, info,id):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        protest=Protest.objects.get(id=id)
        return Donation.objects.filter(protest=protest).order_by("-amount")b
    

class CreateDonation(graphene.Mutation):
    new = graphene.Field(Donations)

    class Arguments:              
        transactionId = graphene.String()
        amount = graphene.Int()
        id=graphene.String()

    def mutate(self, info, transactionId, amount, id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        protest=Protest.objects.get(id=id)
        temp = Donation.objects.create(transactionId=transactionId, amount=amount,made_to=protest)
        temp.save()

        return CreateDonation(new=temp)


class Mutation(graphene.ObjectType):
    create_donation = CreateDonation.Field()