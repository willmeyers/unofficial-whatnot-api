# unofficial-whatnot-api

An unofficial wrapper for whatnot's API.

## Install

```
pip install whatnot
```

## Documentation

```python
from whatnot import What

what = What(email='myemail@example.com', password='mypassword')
```

#### What(email: str = None, password: str = None)

Constructor that initializes a new What instance. If the correct
credentials are provided, your authorization token is cached.

#### am_i() -> dict

Returns a dictionary of all your profile information.

#### my_offers(first: int = 10, after: str = None, sort: str = 'CREATE_AT_ASC') -> dict

Returns a dictionary of all your current negotiations.

#### my_orders(first: int = 10, after: str = None) -> dict

Returns a dictionary of all your current orders.

#### my_live_sales() -> dict

Returns a dictionary of all your current live sales.

#### search(query: str, filters: dict = None, size: int = 30, page: int = 1, sortBy: str = 'Relevance') -> dict

Returns a dictionary of results that match a query.

*query* A query string

*filters* a dictionary of valid filters to apply

**Valid Filters**

*Note: filters values are exactly the same as the facets on whatnot.com*

- in_stock: bool

- category: list[str]

- prices: list[str]

- product_line: list[str]

- years: list[str]

- cards_set__profile: list[str]

Example:
```python
from whatnot import What

what = What()

what.search(query='base set pikachu', filters={'in_stock': True})
```
#### get_product_by_slug(slug: str, listing_condition: int = None, listings_per_page: int = 10) -> dict

Returns a dictionary of a product information based on its URL slug.

#### get_product_estimated_value(product_id: str) -> dict

Returns the estimated price found on the product page.

#### get_product_stats(product_id: str) -> dict

#### get_product_sales_history(product_id: str) -> dict

Returns a dictionary of a products' sales history.

#### get_raffle_drops(before: str = None, after: str = None, first: int = None, last: int = None) ->

Returns a dictionary of a raffle drops in a given date range.

#### get_livestreams(status: str = 'playing') -> dict

Returns a dictionary of livestreams.

- status: str (must be 'playing', 'ended', 'created', 'cancelled', or 'stopped')

#### get_users(username: str, before: str = None, after: str = None, first: int = None, last: int = None)

Returns a dictionary of users.

- username: str (users that contain the query will be returned)




