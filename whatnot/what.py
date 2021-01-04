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
        resp = mutate(query='', variables={})

        return resp

    def am_i(self) -> dict:
        if access_token is None:
            raise NotAuthenticated()

        resp = query()

    def my_offers(self) -> dict:
        if access_token is None:
            raise NotAuthenticated()

        pass

    def my_orders(self) -> dict:
        if access_token is None:
            raise NotAuthenticated()

        pass

    def my_live_sales(self) -> dict:
        if access_token is None:
            raise NotAuthenticated()

        pass

    def search(self, query: str, filters: dict = None, size: int = 30, sort_by: str = 'Relevance') -> dict:
        variables = {
            'size': size
            'sortBy': sort_by
        }

        if filters:
            variables['filters'] = json.dumps(filters)

        resp = query()

        return resp

    def get_product_by_slug(slug: str, listings_per_page: int = 10, listing_condition: int = None) -> dict:
        pass

    def get_product_estimated_value(product_id: str) -> dict:
        pass

    def get_product_stats(product_id: str) -> dict:
        pass

    def get_raffle_drops(before: str = None, after: str = None, first: int = None, last: int = None) -> dict:
        pass
