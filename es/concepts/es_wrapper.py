from elasticsearch import Elasticsearch

ECOMMERCE_INDEX = "ecommerce"

class ES:
    def __new__(self, username=None, password=None, port_host="http://localhost:9200"):
        if username and password:
            es = Elasticsearch([port_host], http_auth=(username, password))
        else:
            es = Elasticsearch([port_host])

        try:
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

    def generic_query(self, queries, aggregations=None, highlights=None, from_=0, size=10, sort=None, script_fields=None, boost_mode=None):
        """
        Perform a generic Elasticsearch query with advanced options.
        Parameters:
        - queries: List of dictionaries representing individual queries with advanced options
        - aggregations: Dictionary representing the aggregation options
        - highlights: Dictionary representing the highlighting options
        - from_: Starting index for pagination
        - size: Number of results per page for pagination
        - sort: Sort options for the query
        - script_fields: Script fields for the query
        - boost_mode: Boost mode for the query
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
            },
            "from": from_,
            "size": size
        }

        for query in queries:
            for condition in query:
                if condition in ["must", "should", "must_not", "filter"]:
                    query_body["query"]["bool"][condition].append(query[condition])

        # Add aggregations if provided
        if aggregations:
            query_body["aggs"] = aggregations

        # Add highlighting if provided
        if highlights:
            query_body["highlight"] = highlights

        # Add sorting if provided
        if sort:
            query_body["sort"] = sort

        # Add script fields if provided
        if script_fields:
            query_body.update(script_fields)

        # Add boost mode if provided
        if boost_mode:
            query_body["query"]["bool"]["boost_mode"] = boost_mode

        # Perform the Elasticsearch query
        result = self.es.search(index=self.index, body=query_body)
        return result

    def create_query(self, query_type, fields, value, options=None):
        if isinstance(fields, str):
            fields = [fields]  # Convert to list if a single field is provided
        query = {query_type: {field: value for field in fields}}
        if options:
            query[query_type].update(options)
        return query

    def format_query(self, *args, **kwargs):
        """
        Perform an Elasticsearch query using the provided parameters and format the response for readability.
        Parameters:
        - *args: Positional arguments for creating the Elasticsearch query
        - **kwargs: Keyword arguments for additional options
        Returns:
        - Formatted Elasticsearch query result
        """
        # Call generic_query method to perform the Elasticsearch query
        query_result = self.generic_query(*args, **kwargs)

        # Format the response for better readability
        formatted_result = {
            "aggr": query_result.get("aggregations", {}),
            "highlight": query_result.get("highlight", {}),
            "result": query_result.get("hits", {}).get("hits", []),
            "pagination": {
                "from": query_result.get("from", 0),
                "size": query_result.get("size", 10),
                "total": query_result.get("hits", {}).get("total", {}).get("value", 0)
            }
            # Add more keys as needed for other response elements
        }

        return formatted_result



if __name__ == "__main__":
    esw = ESWrapper(ES())

    print("Example 1: Simple Match Query for a Specific Category")
    category_match_query = esw.create_query("match", "categories.category_name", "Electronics")
    print("Category Match Query:", category_match_query)
    category_result = esw.format_query([category_match_query])
    print("Category Result:", category_result)
    print()

    print("Example 2: Match Query with Fuzziness and Minimum Should Match")
    fuzzy_min_should_match_query = esw.create_query("match", "description", "compact", {"fuzziness": "AUTO", "minimum_should_match": "75%"})
    print("Fuzzy Match Query with Minimum Should Match:", fuzzy_min_should_match_query)
    fuzzy_min_should_match_result = esw.format_query([fuzzy_min_should_match_query])
    print("Fuzzy Match Result:", fuzzy_min_should_match_result)
    print()

    print("Example 3: Match Query with Wildcard")
    wildcard_query = esw.create_query("wildcard", "name.keyword", "S*")
    print("Wildcard Match Query:", wildcard_query)
    wildcard_result = esw.format_query([wildcard_query])
    print("Wildcard Match Result:", wildcard_result)
    print()

    print("Example 4: Match Query with Prefix")
    prefix_query = esw.create_query("prefix", "name", "Smart")
    print("Prefix Match Query:", prefix_query)
    prefix_result = esw.format_query([prefix_query])
    print("Prefix Match Result:", prefix_result)
    print()

    print("Example 5: Match Query with Range")
    range_query = esw.create_query("range", "price", {"gte": 1000, "lte": 2000})
    print("Range Match Query:", range_query)
    range_result = esw.format_query([range_query])
    print("Range Match Result:", range_result)
    print()

    print("Example 6: Match Query with Exists Condition")
    exists_query = esw.create_query("exists", "attributes.Color", None)
    print("Exists Match Query:", exists_query)
    exists_result = esw.format_query([exists_query])
    print("Exists Match Result:", exists_result)
    print()

    print("Example 7: Match Query with Bool Must and Should Conditions")
    bool_query = [
        esw.create_query("bool", "must", {"match": {"name": "Smartphone"}}),
        esw.create_query("bool", "should", {"match": {"attributes.Color": "Black"}})
    ]
    print("Bool Match Query:", bool_query)

    bool_result = esw.format_query(bool_query)
    print("Bool Match Result:", bool_result)
    print()

    print("Example 8: Match Query with Fuzziness and Minimum Should Match for Multiple Fields")
    multi_field_query = esw.create_query("match", ["name", "description"], "smartphone", {"fuzziness": "AUTO", "minimum_should_match": "75%"})
    print("Multi-field Match Query with Minimum Should Match:", multi_field_query)
    multi_field_result = esw.format_query([multi_field_query])
    print("Multi-field Match Result:", multi_field_result)
    print()

    print("Example 9: Match Query with Boost using create_query method")
    boosted_query = esw.create_query("bool", "should", {"match": {"name": {"query": "smartphone", "boost": 2}}})

    print("Boosted Query:", boosted_query)
    boosted_result = esw.format_query([boosted_query])
    print("Result:", boosted_result)
    print()

    print("Example 10: Match Query with Multi-Match")
    multi_match_query = {
        "multi_match": {
            "query": "smartphone features",
            "fields": ["name", "description"],
            "fuzziness": "AUTO"
        }
    }
    print("Multi-Match Query:", multi_match_query)
    multi_match_result = esw.format_query([multi_match_query])
    print("Multi-Match Result:", multi_match_result)
    print()

    print("Example 11: Combined Query with Bool Must and Should Conditions")
    combined_query = [
        esw.create_query("bool", "must", {"match": {"name": "Smartphone"}}),
        esw.create_query("bool", "should", {"match": {"attributes.Color": "Black"}}),
        esw.create_query("bool", "must_not", {"range": {"price": {"gte": 1000}}})
    ]
    print("Combined Query:", combined_query)
    combined_result = esw.format_query(combined_query)
    print("Combined Query Result:", combined_result)
    print()

    # 1. never using term, as its exact match 
    # 2. .keyword for wild card 
    # 3. dictioary for nested data, so for sort by inner column 
    # 4. geo location 
    # 5. mostly using filter and match  only for geo location. Can use should should, 
    #  filter will have query , should have match or filter 

    # Example 12: Match Query with Exists Condition and Must Not Range Condition
    exists_query = esw.create_query("bool", "must_not", {"range": {"price": {"gte": 1000, "lte": 2000}}})
    print("Exists Match Query with Must Not Range Condition:", exists_query)
    exists_result = esw.format_query([exists_query])
    print("Result:", exists_result)
    print()

    # Example 13: Match Query with Term and Prefix
    print("Example 13: Match Query with Term and Prefix")
    term_prefix_query = [
        esw.create_query("term", "attributes.Color", "Black"),
        esw.create_query("prefix", "name", "S")
    ]
    print("Term and Prefix Query:", term_prefix_query)
    term_prefix_result = esw.format_query(term_prefix_query)
    print("Term and Prefix Result:", term_prefix_result)
    print()

    # Example 14: Match Query with Wildcard and Range
    print("Example 14: Match Query with Wildcard and Range")
    wildcard_range_query = [
        esw.create_query("wildcard", "name.keyword", "S*"),
        esw.create_query("range", "price", {"gte": 500, "lte": 1500})
    ]
    print("Wildcard and Range Query:", wildcard_range_query)
    wildcard_range_result = esw.format_query(wildcard_range_query)
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
    fuzzy_term_exists_result = esw.format_query(fuzzy_term_exists_query)
    print("Fuzzy, Term, and Must Not Exists Result:", fuzzy_term_exists_result)

    print("Example 16: Match Query with Range and Boost")
    range_boost_query = esw.create_query("bool", "must", {"match": {"name": "smartphone"}})
    range_boost_query["bool"]["should"] = esw.create_query("range", "price", {"gte": 1000, "lte": 2000, "boost": 1.5})
    print("Range and Boost Query:", range_boost_query)
    range_boost_result = esw.format_query([range_boost_query])
    print("Range and Boost Result:", range_boost_result)
    print()


    print("Example 17: Match Phrase Query")
    match_phrase_query = esw.create_query("match_phrase", "description", "high-quality smartphone")
    print("Match Phrase Query:", match_phrase_query)
    match_phrase_result = esw.format_query([match_phrase_query])
    print("Match Phrase Result:", match_phrase_result)
    print()



    print("Example 18: Combined Query with Should and Minimum Should Match")
    combined_should_query = [
        esw.create_query("bool", "should", {"match": {"name": "Smartphone", "minimum_should_match": "75%"}}),
        esw.create_query("bool", "should", {"match": {"attributes.Color": "Black"}})
    ]
    print("Combined Should Query with Minimum Should Match:", combined_should_query)

    # Perform the combined query
    combined_should_result = esw.format_query(combined_should_query)
    print("Combined Should Result:", combined_should_result)
    print()


    print("Example 19: Match Query with Prefix and Boost")
    prefix_boost_query = esw.create_query("bool", "must", {"prefix": {"name": "smart"}})
    prefix_boost_query["bool"]["should"] = {"match": {"description": {"query": "features", "boost": 1.5}}}
    print("Prefix and Boost Query:", prefix_boost_query)
    prefix_boost_result = esw.format_query([prefix_boost_query])
    print("Prefix and Boost Result:", prefix_boost_result)
    print()


    print("Example 20: Match Query with Fuzzy, Term, and Filter")
    fuzzy_term_filter_query = [
        esw.create_query("match", "name", "smartphone", {"fuzziness": "AUTO"}),
        esw.create_query("term", "brand", "Samsung"), # EXact match
        esw.create_query("bool", "filter", {"range": {"price": {"lte": 1500}}})
    ]
    print("Fuzzy, Term, and Filter Query:", fuzzy_term_filter_query)
    fuzzy_term_filter_result = esw.format_query(fuzzy_term_filter_query)
    print("Fuzzy, Term, and Filter Result:", fuzzy_term_filter_result)
    print()

    # Example 21: Match Query with Nested Fields and Aggregation
    print("Example 21: Match Query with Nested Fields and Aggregation")
    nested_query = {'nested': {'path': 'variants', 'query': {'match': {'variants.color': 'black'}}}}
    aggregation_body = {'brands_agg': {'terms': {'field': 'brand.keyword'}}}
    nested_result = esw.format_query([nested_query], aggregations=aggregation_body)
    print("Nested Query Result with Aggregation:", nested_result)
    print()

    # Example 22: Match Query with Highlighting
    print("Example 22: Match Query with Highlighting")
    match_highlight_query = esw.create_query("match", "description", "smartphone")
    highlight_body = {'fields': {'description': {}}}
    match_highlight_result = esw.format_query([match_highlight_query], highlights=highlight_body)
    print("Match Query Result with Highlighting:", match_highlight_result)
    print()

    # Example 23: Match Query with Pagination
    print("Example 23: Match Query with Pagination")
    match_pagination_query = esw.create_query("match", "name", "smartphone")
    pagination_result = esw.format_query([match_pagination_query], from_=0, size=5)
    print("Pagination Result:", pagination_result)
    print()


    # Example 24: Match All Query with Sort
    print("Example 24: Match All Query with Sort")
    match_all_sort_query = {"match_all": {}}
    sort_body = [{"price": {"order": "asc"}}]
    match_all_sort_result = esw.format_query([match_all_sort_query], sort=sort_body, from_=0, size=5)
    print("Match All Query Result with Sort:", match_all_sort_result)
    print()

    # Example 25: Match Phrase Prefix Query
    print("Example 25: Match Phrase Prefix Query")
    match_phrase_prefix_query = esw.create_query("match_phrase_prefix", "name", "smart")
    match_phrase_prefix_result = esw.format_query([match_phrase_prefix_query])
    print("Match Phrase Prefix Query Result:", match_phrase_prefix_result)
    print()


    # Example 26: Term Query with Aggregation
    print("Example 26: Term Query with Aggregation")
    term_query = esw.create_query("term", "brand.keyword", "Samsung")
    term_aggregation_body = {"avg_price": {"avg": {"field": "price"}}}
    term_result = esw.format_query([term_query], aggregations=term_aggregation_body)
    print("Term Query Result with Aggregation:", term_result)
    print()

    # Example 27: Bool Query with Filter Aggregation
    print("Example 27: Bool Query with Filter Aggregation")
    bool_query = [
        esw.create_query("bool", "must", {"match": {"name": "smartphone"}}),
        esw.create_query("bool", "filter", {"range": {"price": {"lte": 1500}}})
    ]
    filter_aggregation_body = {
        "price_ranges": {
            "range": {
                "field": "price",
                "ranges": [{"from": 0, "to": 500}, {"from": 501, "to": 1000}, {"from": 1001, "to": 1500}]
            }
        }
    }
    bool_result = esw.format_query(bool_query, aggregations=filter_aggregation_body)
    print("Bool Query Result with Filter Aggregation:", bool_result)
    print()

    # Example 28: Match Query with Scripted Field and Sort
    print("Example 28: Match Query with Scripted Field and Sort")
    match_query = esw.create_query("match", "name", "smartphone")
    scripted_field_body = {
        "_source": {"includes": ["name", "price", "rating"]},
        "script_fields": {
            "discounted_price": {"script": {"source": "doc['price'].value * 0.9"}}
        }
    }
    sort_body = {"price": {"order": "asc"}}
    match_script_sort_result = esw.format_query([match_query], script_fields=scripted_field_body, sort=sort_body)
    print("Match Query Result with Scripted Field and Sort:", match_script_sort_result)
    print()


    # Example 29: Match Query with Boost Mode
    print("Example 29: Match Query with Boost Mode")
    boost_mode_body = {"query": {"match": {"name": {"query": "smartphone features", "boost": 2}}}}
    match_boost_result = esw.format_query([boost_mode_body])
    print("Match Query Result with Boost Mode:", match_boost_result)
    print()

    # Example 30: Exists Query
    print("Example 30: Exists Query")
    exists_query = esw.create_query("exists", "reviews", True)
    print("Exists Query:", exists_query)
    exists_result = esw.format_query([exists_query])
    print("Exists Query Result:", exists_result)
    print()





