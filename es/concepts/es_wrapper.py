from elasticsearch import Elasticsearch

ECOMMERCE_INDEX = "ecommerce"

class ES:
    def __new__(self, username=None, password=None, port_host="http://localhost:9200"):
        # Elasticsearch built-in security features are not enabled. Without authentication, your cluster could be accessible to anyone
        ## For testing not disabled password.
        if username and password:
            es = Elasticsearch([port_host], http_auth=(username, password))
        else:
            es = Elasticsearch([port_host])

        try:
            # Check if the Elasticsearch cluster is healthy
            cluster_health = es.cluster.health()
            if cluster_health['status'] == 'green':
                print("Elasticsearch cluster is healthy.")
            elif cluster_health['status'] == 'yellow':
                print("""Elasticsearch will never assign a replica to the same node as the primary shard, so if you only have one node it is perfectly normal and expected for your cluster to indicate yellow. If you feel better about it being green, then change the number of replicas on each index to be 0.Ja""")
            else:
                print(f"Elasticsearch cluster status: {cluster_health['status']}")
        except exceptions.ConnectionError:
            print("Failed to connect to Elasticsearch. Please check your connection settings.")
        return es

class ESWrapper:
    def __init__(self, es, default_index=ECOMMERCE_INDEX):
        self.es = es
        self.index = default_index

    def set_index(self, index_to_be_set):
        self.index = index_to_be_set

    def generic_query(self, queries):
        """
        Perform a generic Elasticsearch query with advanced options.
        Parameters:
        - queries: List of dictionaries representing individual queries with advanced options
        Returns:
        - Elasticsearch query result
        """
        query_body = {
            "query": {
                "bool": {
                    "must": [],
                    "should": [],
                    "must_not": [],
                    "filter": []
                }
            }
        }

        for query in queries:
            for condition in query:
                if condition in ["must", "should", "must_not", "filter"]:
                    query_body["query"]["bool"][condition].append(query[condition])

        # Perform the Elasticsearch query
        result = self.es.search(index=self.index, body=query_body)
        return result

    def create_query(self, query_type, fields, value, options=None):
        """
        Create an Elasticsearch query with advanced options.
        Parameters:
        - query_type: Type of query (e.g., must, must_not, should, filter)
        - fields: Field names for the query (str or list of str)
        - value: Value for the query
        - options: Dictionary of advanced options for the query (optional)
        Returns:
        - Dictionary representing the Elasticsearch query
        """
        if isinstance(fields, str):
            fields = [fields]  # Convert to list if a single field is provided
        query = {query_type: {field: value for field in fields}}
        if options:
            query[query_type].update(options)
        return query

    def create_multi_match_query(self, fields, query, options=None):
        """
        Create a Multi Match Query with the specified fields, query, and options.
        Args:
        - fields (str or list of str): The fields to search within.
        - query (str): The search query.
        - options (dict, optional): Additional options for the Multi Match Query.
        Returns:
        - dict: The Multi Match Query.
        """
        multi_match_query = {
            "multi_match": {
                "query": query,
                "fields": fields
            }
        }
        if options:
            multi_match_query["multi_match"].update(options)
        return multi_match_query

esw = ESWrapper(ES())

if __name__ == "__main__":
    esw = ESWrapper(ES())
    # Example 1: Simple match query for a specific category
    print("Example 1: Simple Match Query for a Specific Category")
    category_match_query = esw.create_query("match", "categories.category_name", "Electronics")
    print("Category Match Query:", category_match_query)
    category_result = esw.generic_query([category_match_query])
    print("Category Result:", category_result)
    print()

    # Example 2: Match query with fuzziness and minimum should match
    print("Example 2: Match Query with Fuzziness and Minimum Should Match")
    fuzzy_min_should_match_query = esw.create_query("match", "description", "compact", {"fuzziness": "AUTO", "minimum_should_match": "75%"})
    print("Fuzzy Match Query with Minimum Should Match:", fuzzy_min_should_match_query)
    fuzzy_min_should_match_result = esw.generic_query([fuzzy_min_should_match_query])
    print("Fuzzy Match Result:", fuzzy_min_should_match_result)
    print()

    # Example 3: Match query with wildcard
    print("Example 3: Match Query with Wildcard")
    wildcard_query = esw.create_query("wildcard", "name.keyword", "S*")
    print("Wildcard Match Query:", wildcard_query)
    wildcard_result = esw.generic_query([wildcard_query])
    print("Wildcard Match Result:", wildcard_result)
    print()

    # Example 4: Match query with prefix
    print("Example 4: Match Query with Prefix")
    prefix_query = esw.create_query("prefix", "name", "Smart")
    print("Prefix Match Query:", prefix_query)
    prefix_result = esw.generic_query([prefix_query])
    print("Prefix Match Result:", prefix_result)
    print()

    # Example 5: Match query with range
    print("Example 5: Match Query with Range")
    range_query = esw.create_query("range", "price", {"gte": 1000, "lte": 2000})
    print("Range Match Query:", range_query)
    range_result = esw.generic_query([range_query])
    print("Range Match Result:", range_result)
    print()

    # Example 6: Match Query with Exists Condition
    print("Example 6: Match Query with Exists Condition")
    exists_query = esw.create_query("exists", "attributes.Color", None)
    print("Exists Match Query:", exists_query)
    exists_result = esw.generic_query([exists_query])
    print("Exists Match Result:", exists_result)
    print()

    # Example 7: Match query with bool must and should conditions
    print("Example 7: Match Query with Bool Must and Should Conditions")
    bool_query = [
        esw.create_query("bool", "must", {"match": {"name": "Smartphone"}}),
        esw.create_query("bool", "should", {"match": {"attributes.Color": "Black"}})
    ]
    print("Bool Match Query:", bool_query)

    # Perform the bool query
    bool_result = esw.generic_query(bool_query)
    print("Bool Match Result:", bool_result)
    print()


    # Example 8: Match query with fuzziness and minimum should match for multiple fields
    print("Example 8: Match Query with Fuzziness and Minimum Should Match for Multiple Fields")
    multi_field_query = esw.create_query("match", ["name", "description"], "smartphone", {"fuzziness": "AUTO", "minimum_should_match": "75%"})
    print("Multi-field Match Query with Minimum Should Match:", multi_field_query)
    multi_field_result = esw.generic_query([multi_field_query])
    print("Multi-field Match Result:", multi_field_result)
    print()

    # Example 9: Match Query with Boost using create_query method
    print("Example 9: Match Query with Boost using create_query method")
    boosted_query = esw.create_query("bool", "should", {"match": {"name": {"query": "smartphone", "boost": 2}}})

    print("Boosted Query:", boosted_query)
    boosted_result = esw.generic_query([boosted_query])
    print("Result:", boosted_result)
    print()

    # Example 10: Match query with multi_match
    print("Example 10: Match Query with Multi-Match")
    multi_match_query = esw.create_multi_match_query(["name", "description"], "smartphone features", {"fuzziness": "AUTO"})
    print("Multi-Match Query:", multi_match_query)
    multi_match_result = esw.generic_query([multi_match_query])
    print("Multi-Match Result:", multi_match_result)
    print()

    # Example 11: Combined Query with Bool Must and Should Conditions
    print("Example 11: Combined Query with Bool Must and Should Conditions")
    combined_query = [
        esw.create_query("bool", "must", {"match": {"name": "Smartphone"}}),
        esw.create_query("bool", "should", {"match": {"attributes.Color": "Black"}}),
        esw.create_query("bool", "must_not", {"range": {"price": {"gte": 1000}}})
    ]
    print("Combined Query:", combined_query)
    combined_result = esw.generic_query(combined_query)
    print("Combined Query Result:", combined_result)
    print()

    # Example 12: Match Query with Exists Condition and Must Not Range Condition
    exists_query = esw.create_query("bool", "must_not", {"range": {"price": {"gte": 1000, "lte": 2000}}})
    print("Exists Match Query with Must Not Range Condition:", exists_query)
    exists_result = esw.generic_query([exists_query])
    print("Result:", exists_result)
    print()

    # Example 13: Match Query with Term and Prefix
    print("Example 13: Match Query with Term and Prefix")
    term_prefix_query = [
        esw.create_query("term", "attributes.Color", "Black"),
        esw.create_query("prefix", "name", "S")
    ]
    print("Term and Prefix Query:", term_prefix_query)
    term_prefix_result = esw.generic_query(term_prefix_query)
    print("Term and Prefix Result:", term_prefix_result)
    print()

    # Example 14: Match Query with Wildcard and Range
    print("Example 14: Match Query with Wildcard and Range")
    wildcard_range_query = [
        esw.create_query("wildcard", "name.keyword", "S*"),
        esw.create_query("range", "price", {"gte": 500, "lte": 1500})
    ]
    print("Wildcard and Range Query:", wildcard_range_query)
    wildcard_range_result = esw.generic_query(wildcard_range_query)
    print("Wildcard and Range Result:", wildcard_range_result)
    print()

    # Example 15: Match Query with Fuzzy, Term, and Must Not Exists
    print("Example 15: Match Query with Fuzzy, Term, and Must Not Exists")
    fuzzy_term_exists_query = [
        esw.create_query("match", "name", "Smartphone", {"fuzziness": "AUTO"}),
        esw.create_query("term", "attributes.Color", "Black"),
        esw.create_query("bool", "must_not", {"exists": {"field": "reviews"}})
    ]
    print("Fuzzy, Term, and Must Not Exists Query:", fuzzy_term_exists_query)
    fuzzy_term_exists_result = esw.generic_query(fuzzy_term_exists_query)
    print("Fuzzy, Term, and Must Not Exists Result:", fuzzy_term_exists_result)

   
    # Example 15: Match Query with Fuzzy, Term, and Must Not Exists
    print("Example 15: Match Query with Fuzzy, Term, and Must Not Exists")
    fuzzy_term_exists_query = [
        esw.create_query("match", "name", "Smartphone", {"fuzziness": "AUTO"}),
        esw.create_query("term", "attributes.Color", "Black"),
        esw.create_query("bool", "must_not", {"exists": {"field": "reviews"}})
    ]
    print("Fuzzy, Term, and Must Not Exists Query:", fuzzy_term_exists_query)
    fuzzy_term_exists_result = esw.generic_query(fuzzy_term_exists_query)
    print("Fuzzy, Term, and Must Not Exists Result:", fuzzy_term_exists_result)

    print("Example 16: Match Query with Range and Boost")
    range_boost_query = esw.create_query("bool", "must", {"match": {"name": "smartphone"}})
    range_boost_query["bool"]["should"] = esw.create_query("range", "price", {"gte": 1000, "lte": 2000, "boost": 1.5})
    print("Range and Boost Query:", range_boost_query)
    range_boost_result = esw.generic_query([range_boost_query])
    print("Range and Boost Result:", range_boost_result)
    print()


    print("Example 17: Match Phrase Query")
    match_phrase_query = esw.create_query("match_phrase", "description", "high-quality smartphone")
    print("Match Phrase Query:", match_phrase_query)
    match_phrase_result = esw.generic_query([match_phrase_query])
    print("Match Phrase Result:", match_phrase_result)
    print()



    print("Example 18: Combined Query with Should and Minimum Should Match")
    combined_should_query = [
        esw.create_query("bool", "should", {"match": {"name": "Smartphone", "minimum_should_match": "75%"}}),
        esw.create_query("bool", "should", {"match": {"attributes.Color": "Black"}})
    ]
    print("Combined Should Query with Minimum Should Match:", combined_should_query)

    # Perform the combined query
    combined_should_result = esw.generic_query(combined_should_query)
    print("Combined Should Result:", combined_should_result)
    print()


    print("Example 19: Match Query with Prefix and Boost")
    prefix_boost_query = esw.create_query("bool", "must", {"prefix": {"name": "smart"}})
    prefix_boost_query["bool"]["should"] = {"match": {"description": {"query": "features", "boost": 1.5}}}
    print("Prefix and Boost Query:", prefix_boost_query)
    prefix_boost_result = esw.generic_query([prefix_boost_query])
    print("Prefix and Boost Result:", prefix_boost_result)
    print()


    print("Example 20: Match Query with Fuzzy, Term, and Filter")
    fuzzy_term_filter_query = [
        esw.create_query("match", "name", "smartphone", {"fuzziness": "AUTO"}),
        esw.create_query("term", "brand", "Samsung"),
        esw.create_query("bool", "filter", {"range": {"price": {"lte": 1500}}})
    ]
    print("Fuzzy, Term, and Filter Query:", fuzzy_term_filter_query)
    fuzzy_term_filter_result = esw.generic_query(fuzzy_term_filter_query)
    print("Fuzzy, Term, and Filter Result:", fuzzy_term_filter_result)
    print()


