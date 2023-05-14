import graphene
from graphene import ObjectType
import gql.query as query


class Query(query.Query, ObjectType):
    pass

# class Mutation(api.schema.Mutation,ObjectType):
#     pass

schema = graphene.Schema(query=Query)
