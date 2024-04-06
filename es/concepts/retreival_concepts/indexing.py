"""

In Elasticsearch, data can be indexed in different ways depending on how you want to manage and organize your data. The two main approaches are explicit indexing and dynamic indexing. Let's explore the difference between these two methods:

1. Explicit Indexing:   *******  es.index(body=record)  *******
                                ----------------------

Definition: Explicit indexing involves manually specifying the index, document ID, and other metadata when indexing data into Elasticsearch.
Usage: You explicitly define the index name (index_name), document ID (_id), and other metadata (e.g., routing, versioning) before indexing the data.

Advantages:
You have full control over the indexing process, including the index structure, document IDs, and metadata.
You can ensure that data is indexed exactly as you want it, with specific settings and mappings.

Disadvantages:
Requires more effort and management, especially when dealing with large datasets or complex indexing requirements.
May lead to more manual errors if metadata is not handled correctly.

2. Dynamic Indexing:  *******  es.index(index=record["_index"], id=record["_id"], body=record["_source"])  *******
                               --------------------------------------------------------------------------

Definition: Dynamic indexing allows Elasticsearch to automatically handle the index creation, document ID generation, and mapping based on the data provided during indexing.
Usage: You provide the data to be indexed without specifying the index name or document ID explicitly. Elasticsearch dynamically creates the index and assigns document IDs as needed.

Advantages:
Simplifies the indexing process by letting Elasticsearch handle index creation, mappings, and document IDs automatically.
Suitable for scenarios where the structure of the data is flexible or when dealing with a large volume of constantly changing data.

Disadvantages:
Less control over the index settings and mappings, which may not be ideal for highly structured data.
Document IDs are auto-generated, which may not always align with your application's requirements.

---------------------------------------
Difference:
The main difference between explicit indexing and dynamic indexing lies in the level of control and automation:

Control: Explicit indexing gives you full control over the indexing process, allowing you to define index settings, mappings, document IDs, and other metadata explicitly. Dynamic indexing automates many of these tasks, letting Elasticsearch handle index creation, mapping generation, and document ID assignment based on the data.

Automation: Dynamic indexing is more automated as Elasticsearch takes care of many indexing details. Explicit indexing requires manual specification of index parameters and metadata.

Choosing Between the Two:

Use explicit indexing when you need precise control over the indexing process, have specific index settings or mappings, 
    *****or require custom document IDs.******
Use dynamic indexing when dealing with ****flexible data structures******, rapid data ingestion, or when you prefer a more hands-off approach to index management.
In your case, using the Python script provided earlier involves explicit indexing, where you manually specify the index name (index_name), document IDs (_id), and other metadata before indexing the data into Elasticsearch. This approach gives you control over how the data is indexed and organized within Elasticsearch.


---**** MAPPING is a different concept than idexing ********* 
A. Mapping
Definition: Defining a schema involves specifying the data types, properties, and settings for each field in your index.
Purpose: It helps Elasticsearch understand the structure of your data, enforce data types, and optimize storage and search operations.
Example: You can define mappings for fields like text, keyword, date, integer, float, boolean, nested, etc., and specify settings such as analyzer, indexing options, fielddata, etc.
Process: Schema definition is done before indexing data and can be static (fixed schema) or dynamic (dynamic mappings based on data structure).

B. Indexing 
Definition: Indexing data is the process of adding documents (JSON objects) to an index in Elasticsearch.
Purpose: It populates the index with data that adheres to the defined schema (mapping) and makes the data searchable.
Example: You index documents with fields like title, description, category, price, etc., into Elasticsearch according to the defined schema.
Process: Indexing can be done explicitly (specifying index name, document ID, etc.) or implicitly (letting Elasticsearch handle index creation, document ID generation, etc.).


Key Differences A and B:

Timing: Defining a schema is a **pre-indexing** step that occurs before data is indexed into Elasticsearch. 
    ***It sets the structure and ***rules for how data should be indexed***.
Purpose: Schema definition ensures data consistency, type enforcement, and optimization of search operations. It helps Elasticsearch understand the data structure and how to handle queries efficiently.
Flexibility: While defining a schema, you can specify field types, analyzers, index settings, etc., to tailor Elasticsearch's behavior. Indexing, on the other hand, is about adding actual data to the index based on the defined schema.
Control: Schema definition gives you control over how fields are interpreted and indexed. Indexing data adheres to the rules and structure defined in the schema.
In summary, defining a schema (mapping) is about setting up the blueprint for how data should be structured and interpreted in Elasticsearch, while indexing data is about adding actual data to the index according to the defined schema. Both processes are essential for effective data management and search capabilities in Elasticsearch.

Explicit Mapping: Use explicit mappings when you have structured data, require strict data validation, want optimized search performance, and need versioning and compatibility control.
Dynamic Mapping: Use dynamic mapping for unstructured or evolving data, quick prototyping, flexibility in data types, and when you prefer automatic handling of mappings.

"""
# es.index(body=record) # Explicit Indexing
# es.index(index=record["_index"], id=record["_id"], body=record["_source"]) # Dynamic Indexing 

# Create index and mapping
import sys
sys.path.insert(0, '..')
from connection import es
index_name = "ecommerce"
mapping = {
    "mappings": {
        "properties": {
            "product_id": {"type": "keyword"},
            "name": {"type": "text"},
            "description": {"type": "text"},
            "price": {"type": "float"},
            "categories": {
                "type": "nested",
                "properties": {
                    "category_id": {"type": "keyword"},
                    "category_name": {"type": "keyword"}
                }
            },
            "attributes": {
                "type": "nested",
                "properties": {
                    "attribute_name": {"type": "keyword"},
                    "attribute_value": {"type": "keyword"}
                }
            },
            "reviews": {
                "type": "nested",
                "properties": {
                    "review_id": {"type": "keyword"},
                    "user_id": {"type": "keyword"},
                    "rating": {"type": "integer"},
                    "comment": {"type": "text"},
                    "timestamp": {"type": "date", "format": "yyyy-MM-dd'T'HH:mm:ssZ"}
                }
            }
        }
    }
}

# Create index with mapping
es.indices.create(index=index_name, body=mapping)

print(f"Mapping created for index '{index_name}'.")

