import graphene
from graphene_django import DjangoObjectType
from .models import Blog
from graphql import GraphQLError
from protestId.models import Protest


class Blogs(DjangoObjectType):
    class Meta:
        model = Blog


class Query(graphene.ObjectType):
    myblog = graphene.List(Blogs,id = graphene.String(required=True))


    def resolve_myblog(self,info,id):
        active=info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        temp = Protest.objects.get(id=id)
        return Blog.objects.filter(protest=temp).order_by("-date")


class AddBlog(graphene.Mutation):
    info = graphene.Field(Blogs)

    class Arguments:
        title = graphene.String()
        body = graphene.String()


    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        blog = Blog.objects.create(author=user)
        blog.title = kwargs.get("title")
        blog.body = kwargs.get("body")

        blog.save()

        return AddBlog(info=blog)


class Mutation(graphene.ObjectType):
    add_blog = AddBlog.Field()