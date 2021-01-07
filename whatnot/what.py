import json

from whatnot.utils import query, mutate
from whatnot.exceptions import NotAuthenticated


class What:
    access_token: str = None

    def __init__(self, email: str = None, password: str = None):
        if email and password is None:
            raise ValueError('missing password')

        if password and email is None:
            raise ValueError('missing email')

        if email and password:
            self.access_token = self._authenticate(email, password)
        
    def _authenticate(self, email: str, password: str) -> str:
        operation_name = 'LoginMutation'

        query = 'mutation LoginMutation($email: String!, $password: String!) {  login(email: $email, password: $password) {    authToken    __typename  }}'

        variables = {
            'email': email,
            'password:': password
        }

        resp = query(operation_name, query, variables)

        return resp

    def am_i(self) -> dict:
        if access_token is None:
            raise NotAuthenticated()

        operation_name = 'me'

        query = 'query me {  me {    email    firstName    lastName    defaultCard {      customerReference      cardMetadata      __typename    }    defaultShippingAddress {      postalCode      line1      line2      city      state      __typename    }    __typename  }}'

        variables = {}

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        resp = query(query, varibles, headers=headers)

        return resp

    def my_offers(self, first: int = 10, cursor: str = None) -> dict:
        if access_token is None:
            raise NotAuthenticated()

        operation_name = 'MyOffers'

        varibles = {
            'first': first
        }

        if cursor:
            varibles['cursor'] = cursor

        query = 'query MyOffers($first: Int, $cursor: String) {  myOfferNegotiations(first: $first, after: $cursor, sort: CREATED_AT_ASC) {    pageInfo {      hasNextPage      hasPreviousPage      endCursor      startCursor      __typename    }    edges {      node {        id        orderId        status        priceCents        createdAt        listing {          id          productName          conditionName          product {            id            name            slug            image {              bucket              key              url              __typename            }            __typename          }          priceCents          images {            key            bucket            url            __typename          }          __typename        }        __typename      }      __typename    }    __typename  }}'

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        resp = query(query, variables, headers=headers)

        return resp

    def my_orders(self, first: int = 10, cursor: str = None) -> dict:
        if access_token is None:
            raise NotAuthenticated()

        operation = 'MyOrders'

        query = 'query MyOrders($first: Int, $cursor: String) {  myOrders(first: $first, after: $cursor) {    pageInfo {      hasNextPage      hasPreviousPage      endCursor      startCursor      __typename    }    edges {      node {        id        totalCents        subtotalCents        taxesCents        shippingPriceCents        createdAt        prettyStatuses        prettyStatus        uuid        status        items {          edges {            node {              id              listing {                title                description                conditionName                images {                  key                  bucket                  __typename                }                __typename              }              product {                id                name                slug                image {                  bucket                  url                  key                  __typename                }                __typename              }              __typename            }            __typename          }          __typename        }        __typename      }      __typename    }    __typename  }}'

        varibles = {
            'first': first
        }

        if cursor:
            varibles['cursor'] = cursor

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        resp = query(query, varibles, headers=headers)

        return resp

    def my_live_sales(self, first, cursor: str = None) -> dict:
        if access_token is None:
            raise NotAuthenticated()

        variables = {
            'first': first
        }

        if cursor:
            varibles['cursor'] = cursor

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        resp = query(query, varibles, headers=headers)

        return resp


    def search(self, query: str, filters: dict = None, size: int = 30, sort_by: str = 'Relevance') -> dict:
        variables = {
            'size': size
            'sortBy': sort_by
        }

        if filters:
            variables['filters'] = json.dumps(filters)

        resp = query(query, varialbles)

        return resp

    def get_product_by_slug(self, slug: str, listings_per_page: int = 10, listing_condition: int = None) -> dict:
        pass

    def get_product_estimated_value(self, product_id: str) -> dict:
        pass

    def get_product_stats(self, product_id: str) -> dict:
        pass

    def get_raffle_drops(self, before: str = None, after: str = None, first: int = None, last: int = None) -> dict:
        pass

    def get_livestreams(self, status: str = 'playing'):
        pass

    def get_users(self, query: str, before: str = None, after: str = None, first: int = None, last: int = None):
        pass
