import requests
import json

def fetch_movie_data():
    url = 'https://query.wikidata.org/sparql'
    query = """
        SELECT ?movie ?movieLabel ?imdb_id ?publication_date WHERE {
            ?movie wdt:P31 wd:Q11424.
            ?movie wdt:P345 ?imdb_id.
            ?movie wdt:P577 ?publication_date.
            FILTER(YEAR(?publication_date) > 2013)
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        }
        ORDER BY ?publication_date
    """
    response = requests.post(url, data={'query': query}, headers={'Accept': 'application/sparql-results+json'})
    data = json.loads(response.text)

    movie_data = []

    for item in data['results']['bindings']:
        movie_data.append({
            'Movie': item['movieLabel']['value'],
            'IMDB ID': item['imdb_id']['value'],
            'Release Date': item['publication_date']['value']
        })

    return movie_data