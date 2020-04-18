from django.utils import timezone

sample_fulfillment_events = [
    {'target_date' : '2020-06-01'},
    {'target_date' : '2020-06-08'}
]

sample_orders = [
    {
        'customer_name': '[NNotARealOrder] Christopher Koliba',
        'customer_address': '11 Lonsdale Place, Dorking',
        'customer_postcode': 'RH4 2WJ',
        'customer_email': 'dev+farmbox1@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Delivery',
        'collection_location': 'Denbies',
        'notes': '04-Mar',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },

    {
        'customer_name': '[NotARealOrder] Mike Jameson',
        'customer_address': '12 Curtis Road, Dorking',
        'customer_postcode': 'RH4 1XD',
        'customer_email': 'dev+farmbox2@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Collection',
        'collection_location': 'Denbies',
        'notes': 'weekly',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },

    {
        'customer_name': '[NotARealOrder] Valerie Bennet',
        'customer_address': 'Cotton Row, Holmbury St. Mary',
        'customer_postcode': 'RH5 6NB',
        'customer_email': 'dev+farmbox3@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Delivery',
        'collection_location': '',
        'notes': 'weekly',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },

    {
        'customer_name': '[NotARealOrder] Chloe Fawcett',
        'customer_address': 'Dial Post Barn, Horsham, West Sussex',
        'customer_postcode': 'RH12 4QX',
        'customer_email': 'dev+farmbox4@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Collection',
        'collection_location': 'Ockley',
        'notes': 'watch out for dog',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    }
]