from elasticsearch import Elasticsearch

# Elasticsearchga ulanish
es = Elasticsearch()

# JSON fayllarni Elasticsearchga yuklash
def index_data(data):
    for i, (key, value) in enumerate(data.items()):
        es.index(index="documents", id=i, body={"key": key, "value": value})

# Qidiruv qilish
def search_es(query):
    response = es.search(index="documents", body={
        "query": {
            "match": {
                "value": query
            }
        }
    })
    for hit in response['hits']['hits']:
        print(hit["_source"])

# JSON fayllarni Elasticsearchga yuklash va qidirish
index_data(data)
search_es("example")
