from django.utils import timezone

sample_fulfillment_events = [
    {'target_date' : '2020-06-01'},
    {'target_date' : '2020-06-08'}
]

sample_orders = [
    {
        'f_number': '1',
        'customer_first_name': '[NNotARealOrder] Christopher',
        'customer_last_name': 'Koliba',
        'customer_address': '11 Lonsdale Place, Dorking',
        'customer_postcode': 'RH4 2WJ',
        'customer_email': 'dev+chriskoliba@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Delivery',
        # 'collection_location': 'Denbies',
        'notes': '04-Mar',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },
    {
        'f_number': '2',
        'customer_first_name': '[NotARealOrder] Mike',
        'customer_last_name': 'Jameson',
        'customer_address': '12 Curtis Road, Dorking',
        'customer_postcode': 'RH4 1XD',
        'customer_email': 'dev+mikejameson@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Delivery',
        # 'collection_location': 'Denbies',
        'notes': 'weekly',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },

    {
        'f_number': '3',
        'customer_first_name': '[NotARealOrder] Valerie',
        'customer_last_name': 'Bennet',
        'customer_address': 'Cotton Row, Holmbury St. Mary',
        'customer_postcode': 'RH5 6NB',
        'customer_email': 'dev+farmbox3@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Delivery',
        # 'collection_location': '',
        'notes': 'weekly',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },

    {
        'f_number': '4',
        'customer_first_name': '[NotARealOrder] Chloe',
        'customer_last_name': 'Fawcett',
        'customer_address': 'Dial Post Barn, Horsham, West Sussex',
        'customer_postcode': 'RH12 4QX',
        'customer_email': 'dev+farmbox4@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Collect from Ockley Shop',
        # 'collection_location': 'Ockley',
        'notes': 'watch out for dog',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },
    {
        'f_number': '5',
        'customer_first_name': '[NotARealOrder] Mavis',
        'customer_last_name': 'Harton',
        'customer_address': 'The Stables, Friars St. North Holmwood',
        'customer_postcode': 'RH5 4QX',
        'customer_email': 'dev+mavisharton@howapped.com',
        'customer_phone': '0789 449 5431',
        'fulfillment_method': 'Delivery',
        # 'collection_location': '',
        'notes': 'Fri weekly until further notice please',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    }
]
