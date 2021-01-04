# unofficial-whatnot-api

An unofficial wrapper for whatnot's API.

## Install

```
pip install whatnot
```

## Documentation

```python
from whatnot import What

w = What('myemail@example.com', 'mypassword')
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

#### get_product_by_slug(slug: str, listing_condition: int, listings_per_page: int = 10) -> dict

Returns a dictionary of a product information based on its URL slug.

