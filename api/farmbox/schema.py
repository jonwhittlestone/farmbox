import graphene
from order import schema

class Query(schema.Query, graphene.ObjectType):
    pass

# class Mutation(order.schema.Mutation, graphene.ObjectType):
#     pass

schema = graphene.Schema(query=Query)