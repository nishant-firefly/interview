from elasticsearch import Elasticsearch
# Create an Elasticsearch client instance
def get_connection(username=None, password=None, port_host="http://localhost:9200" ):
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
        else:
            print(f"Elasticsearch cluster status: {cluster_health['status']}")
    except exceptions.ConnectionError:
        print("Failed to connect to Elasticsearch. Please check your connection settings.")
    return es

if __name__=="__main__":
    es = get_connection()