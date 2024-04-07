from elasticsearch import Elasticsearch
ECOMMERCE_INDEX="ecommerce"
class ES:
    def __new__(self,username=None, password=None, port_host="http://localhost:9200" ):
        # 
        # Elasticsearch built-in security features are not enabled. Without authentication, your cluster could be accessible to anyone
        ## For testing not disabled password.
        if username and password:
            es = Elasticsearch([port_host], http_auth=(username, password))
        else:
            es=  Elasticsearch([port_host])

        try:
            # Check if the Elasticsearch cluster is healthy
            cluster_health = es.cluster.health()
            if cluster_health['status'] == 'green':
                print("Elasticsearch cluster is healthy.")
            elif cluster_health['status']=='yellow':
                print("""Elasticsearch will never assign a replica to the same node as the primary shard, so if you only have one node it is perfectly normal and expected for your cluster to indicate yellow. If you feel better about it being green, then change the number of replicas on each index to be 0.Ja""")
            else:
                print(f"Elasticsearch cluster status: {cluster_health['status']}")
        except exceptions.ConnectionError:
            print("Failed to connect to Elasticsearch. Please check your connection settings.")
        return es



class ESWrapper:
    def __init__(self, es, default_index=ECOMMERCE_INDEX) -> None:
        self.es=es
        self.index = ECOMMERCE_INDEX 
    def search(self, k_v):
        # Simple Match Query
        # e.g  k_v= {"name": "product"}
        query = {"query": {"match": k_v}}
        result = self.es.search(index=self.index, body=query)
        return [hit["_source"] for hit in result['hits']['hits']]
        breakpoint()
        self.es.search()

        # Execute the Match Query
        

        # Print the matched documents
        print("Matched Documents:")
        for hit in result['hits']['hits']:
            print(hit['_source'])
    
if __name__=="__main__":
    esw = ESWrapper(ES())
    smart_phone_x= [{'product_id': 'P001', 'name': 'Smartphone X', 'description': 'A high-performance smartphone with advanced features.', 'price': 999.99, 'categories': [{'category_id': 'C001', 'category_name': 'Electronics'}, {'category_id': 'C002', 'category_name': 'Mobile Phones'}], 'attributes': [{'attribute_name': 'Brand', 'attribute_value': 'XCorp'}, {'attribute_name': 'Color', 'attribute_value': 'Black'}, {'attribute_name': 'RAM', 'attribute_value': '8GB'}, {'attribute_name': 'Storage', 'attribute_value': '128GB'}], 'reviews': [{'review_id': 'R001', 'user_id': 'U001', 'rating': 4, 'comment': 'Great phone!', 'timestamp': '2023-04-15T12:00:00Z'}, {'review_id': 'R002', 'user_id': 'U002', 'rating': 5, 'comment': 'Amazing features.', 'timestamp': '2023-04-16T09:30:00Z'}]}]
    assert(esw.search({"name":"Smartphone X"})==smart_phone_x)
