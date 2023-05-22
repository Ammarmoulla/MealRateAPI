import graphene
from graphene import ObjectType
import gql.query
import gql.mutation


class Query(gql.query.Query, 
            ObjectType):
    pass

class Mutation(gql.mutation.Mutation,
               ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
