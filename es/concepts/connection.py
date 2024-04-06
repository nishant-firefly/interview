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
if __name__=="__main__":
    es = ES()