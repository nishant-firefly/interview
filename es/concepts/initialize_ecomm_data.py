from es_wrapper import ES, ECOMMERCE_INDEX
es=ES()
# Sample data records for indexing
data_records = [
    {
        "product_id": "P001",
        "name": "Smartphone X",
        "description": "A high-performance smartphone with advanced features.",
        "price": 999.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C002", "category_name": "Mobile Phones" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "XCorp" },
            { "attribute_name": "Color", "attribute_value": "Black" },
            { "attribute_name": "RAM", "attribute_value": "8GB" },
            { "attribute_name": "Storage", "attribute_value": "128GB" }
        ],
        "reviews": [
            { "review_id": "R001", "user_id": "U001", "rating": 4, "comment": "Great phone!", "timestamp": "2023-04-15T12:00:00Z" },
            { "review_id": "R002", "user_id": "U002", "rating": 5, "comment": "Amazing features.", "timestamp": "2023-04-16T09:30:00Z" }
        ]
    },
    {
        "product_id": "P002",
        "name": "Laptop Y",
        "description": "A powerful laptop for work and gaming.",
        "price": 1499.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C003", "category_name": "Laptops" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "YTech" },
            { "attribute_name": "Color", "attribute_value": "Silver" },
            { "attribute_name": "RAM", "attribute_value": "16GB" },
            { "attribute_name": "Storage", "attribute_value": "512GB SSD" }
        ],
        "reviews": [
            { "review_id": "R003", "user_id": "U003", "rating": 5, "comment": "Great performance.", "timestamp": "2023-04-17T10:45:00Z" },
            { "review_id": "R004", "user_id": "U004", "rating": 4, "comment": "Good for gaming.", "timestamp": "2023-04-18T14:20:00Z" }
        ]
    },
    {
        "product_id": "P003",
        "name": "Smart TV Z",
        "description": "A large-screen smart TV with 4K resolution.",
        "price": 1999.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C004", "category_name": "Televisions" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "ZTech" },
            { "attribute_name": "Screen Size", "attribute_value": "55 inches" },
            { "attribute_name": "Resolution", "attribute_value": "4K Ultra HD" },
            { "attribute_name": "Smart Features", "attribute_value": "Built-in apps, voice control" }
        ],
        "reviews": [
            { "review_id": "R005", "user_id": "U005", "rating": 4, "comment": "Excellent picture quality.", "timestamp": "2023-04-19T11:10:00Z" },
            { "review_id": "R006", "user_id": "U006", "rating": 3, "comment": "Smart features need improvement.", "timestamp": "2023-04-20T15:30:00Z" }
        ]
        },
        {
        "product_id": "P004",
        "name": "Wireless Headphones A",
        "description": "High-quality wireless headphones with noise cancellation.",
        "price": 299.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C005", "category_name": "Audio" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "ATech" },
            { "attribute_name": "Color", "attribute_value": "Black" },
            { "attribute_name": "Wireless Technology", "attribute_value": "Bluetooth 5.0" },
            { "attribute_name": "Noise Cancellation", "attribute_value": "Active" }
        ],
        "reviews": [
            { "review_id": "R007", "user_id": "U007", "rating": 5, "comment": "Great sound quality.", "timestamp": "2023-04-21T08:45:00Z" }
        ]
    },
    {
        "product_id": "P005",
        "name": "Digital Camera B",
        "description": "Compact digital camera with high-resolution imaging.",
        "price": 499.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C006", "category_name": "Cameras" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "BTech" },
            { "attribute_name": "Resolution", "attribute_value": "20 megapixels" },
            { "attribute_name": "Zoom", "attribute_value": "10x optical zoom" },
            { "attribute_name": "Video Recording", "attribute_value": "4K UHD" }
        ],
        "reviews": [
            { "review_id": "R008", "user_id": "U008", "rating": 4, "comment": "Great for capturing memories.", "timestamp": "2023-04-22T13:20:00Z" }
        ]
        },
        {
        "product_id": "P006",
        "name": "Fitness Tracker C",
        "description": "Smart fitness tracker with heart rate monitoring.",
        "price": 149.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C007", "category_name": "Wearables" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "CTech" },
            { "attribute_name": "Color", "attribute_value": "Blue" },
            { "attribute_name": "Features", "attribute_value": "Step counter, sleep tracking" }
        ],
        "reviews": [
            { "review_id": "R009", "user_id": "U009", "rating": 5, "comment": "Very accurate heart rate monitoring.", "timestamp": "2023-04-23T10:00:00Z" }
        ]
    },
    {
        "product_id": "P007",
        "name": "Gaming Console D",
        "description": "Next-gen gaming console for immersive gaming experiences.",
        "price": 599.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C008", "category_name": "Gaming" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "DTech" },
            { "attribute_name": "Color", "attribute_value": "Black" },
            { "attribute_name": "Storage", "attribute_value": "1TB SSD" }
        ],
        "reviews": [
            { "review_id": "R010", "user_id": "U010", "rating": 5, "comment": "Amazing gaming performance.", "timestamp": "2023-04-24T15:45:00Z" }
        ]
    },
    {
        "product_id": "P008",
        "name": "Wireless Router E",
        "description": "High-speed wireless router for home and office use.",
        "price": 99.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C009", "category_name": "Networking" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "ETech" },
            { "attribute_name": "Speed", "attribute_value": "AC3200" },
            { "attribute_name": "Connectivity", "attribute_value": "Dual-band Wi-Fi" }
        ],
        "reviews": [
            { "review_id": "R011", "user_id": "U011", "rating": 4, "comment": "Good range and speed.", "timestamp": "2023-04-25T11:30:00Z" }
        ]
    },
    {
        "product_id": "P009",
        "name": "Smart Home Hub F",
        "description": "Central hub for controlling smart home devices.",
        "price": 199.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C010", "category_name": "Smart Home" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "FTech" },
            { "attribute_name": "Compatibility", "attribute_value": "Works with Alexa, Google Assistant" }
        ],
        "reviews": [
            { "review_id": "R012", "user_id": "U012", "rating": 4, "comment": "Easy setup and integration.", "timestamp": "2023-04-26T09:15:00Z" }
        ]
    },
    {
        "product_id": "P010",
        "name": "Portable Bluetooth Speaker G",
        "description": "Compact and portable speaker with Bluetooth connectivity.",
        "price": 79.99,
        "categories": [
            { "category_id": "C001", "category_name": "Electronics" },
            { "category_id": "C005", "category_name": "Audio" }
        ],
        "attributes": [
            { "attribute_name": "Brand", "attribute_value": "GTech" },
            { "attribute_name": "Color", "attribute_value": "Red" },
            { "attribute_name": "Battery Life", "attribute_value": "10 hours" }
        ],
        "reviews": [
            { "review_id": "R013", "user_id": "U013", "rating": 5, "comment": "Excellent sound quality for its size.", "timestamp": "2023-04-27T14:00:00Z" }
        ]
    }
]

# Bulk indexing of data records
bulk_data = []
for record in data_records:
    bulk_data.append({"index": {"_index": ECOMMERCE_INDEX, "_id": record["product_id"]}})
    bulk_data.append(record)

# Perform bulk indexing
es.bulk(body=bulk_data)

print("*** Even if rerun it will be same number of records, no duplicate *** \n \
      Schema defined and data indexed successfully.")
