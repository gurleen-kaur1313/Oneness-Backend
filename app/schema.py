import graphene
import graphql_jwt
import user.schema
import blog.schema
import protestId.schema
import ngo.schema
import emergency.schema
import resources.schema
import location.schema
import donations.schema


class Query(user.schema.Query, blog.schema.Query, protestId.schema.Query, ngo.schema.Query, emergency.schema.Query, resources.schema.Query, location.schema.Query, donations.schema.Query, graphene.ObjectType):
    pass


class Mutation(user.schema.Mutation, blog.schema.Mutation, protestId.schema.Query, ngo.schema.Mutation, emergency.schema.Mutation, resources.schema.Mutation, location.schema.Mutation, donations.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)