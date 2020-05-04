import graphene
import order.schema
import product.schema

class Query(order.schema.Query, product.schema.Query, graphene.ObjectType):
    pass

# class Mutation(order.schema.Mutation, graphene.ObjectType):
#     pass

schema = graphene.Schema(query=Query, mutation=None)
