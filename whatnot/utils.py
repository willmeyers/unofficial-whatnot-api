import requets


BASE_URL = 'https://api.whatnot.com/graphql/'


def query(query, variables):
    resp = requets.post(f'{BASE_URL}',
        params=variables,
        data={
            'query': query
        }
    )

    return resp.json()


def send_mutation(query, variables):
    resp = requets.post(f'{BASE_URL}',
        params=variables,
        data={
            'query': query
        }
    )

    return resp.json()
