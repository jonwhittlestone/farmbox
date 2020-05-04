import graphene
from graphene_django import DjangoObjectType

from .models import Order


class OrderType(DjangoObjectType):
    class Meta:
        model = Order

class Query(graphene.ObjectType):
    orders = graphene.List(OrderType)

    def resolve_orders(self, info):
        return Order.objects.all()

# class CreateOrder(graphene.Mutation):
#     order = graphene.Field(OrderType)

#     class Arguments:
#         customer_name = graphene.String()

    # def mutate(self, info, **kwargs):
        '''Resolver function for mutation'''
        # order = Order.create(**kwargs)
        # product = Product(title=kwargs.get('title'), price_ex_vat=kwargs.get(
        #     'price_ex_vat'), isbn=kwargs.get('isbn'))

        # product.save()
        # return CreateProduct(product=product)

# class Mutation(graphene.ObjectType):
#     pass
#     create_order = CreateOrder.Field()


schema = graphene.Schema(query=Query)
