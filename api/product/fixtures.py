from django.conf import settings
from djmoney.money import Money

initial_products = [
    {
        'name': 'Village Greens Veg Bag : Large FV3355',
        'code': 'village-greens-veg-bag-large',
        'pack_size': '9-10 lines',
        'price': Money(15, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':1,
        'category': settings.PRODUCT_CATEGORIES_VEGBAG,
    },

    {
        'name': 'Village Greens Veg Bag - Medium  FV0083',
        'code': 'village-greens-veg-bag-medium',
        'pack_size': '8-9 lines',
        'price': Money(13, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':2,
        'category': settings.PRODUCT_CATEGORIES_VEGBAG
    },
    {
        'name': 'Village Greens Veg Bag : Small FV3354',
        'code': 'village-greens-veg-bag-small',
        'pack_size': '7-8 lines',
        'price': Money(11, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':3,
        'category': settings.PRODUCT_CATEGORIES_VEGBAG
    },
    {
        'name': 'Asparagus FV0092',
        'code': 'asparagus',
        'pack_size': '250g',
        'price': Money(2.95, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':4,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Fine green beans FV0226',
        'code': 'fine-green-beans',
        'pack_size': '250g',
        'price': Money(2.45, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':5,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Broccoli FV0011',
        'code': 'broccoli',
        'pack_size': 'Head appr 400g',
        'price': Money(1.25, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':6,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Butternut Squash FV0013',
        'code': 'butternut-squash',
        'pack_size': '1',
        'price': Money(1.35, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':7,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'name': 'Cabbage Hispi FV0087',
        'code': 'cabbage-hispi',
        'pack_size': '1',
        'price': Money(1.8, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':8,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'name': 'Cabbage Savoy FV0104',
        'code': 'cabbage-savoy',
        'pack_size': '1',
        'price': Money(2.75, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':9,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Cabbage Red FV0016',
        'code': 'cabbage-red',
        'pack_size': '1',
        'price': Money(0.7, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':10,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Carrots : loose washed FV0017',
        'code': 'carrots-loose',
        'pack_size': '500g',
        'price': Money(0.6, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':11,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Cauliflower FV0109',
        'code': 'cauliflower',
        'pack_size': '1',
        'price': Money(3.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':12,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Courgette FV0021',
        'code': 'courgette',
        'pack_size': '500g',
        'price': Money(1.28,settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':13,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':14,
        'name': 'Leeks FV0059',
        'code': 'leeks',
        'pack_size': '500g',
        'price': Money(1.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':15,
        'name': 'Mushroom Cup FV0145',
        'code': 'mushroom-cup',
        'pack_size': '150g',
        'price': Money(0.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':16,
        'name': 'Onions FV0028',
        'code': 'onions',
        'pack_size': '500g',
        'price': Money(0.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':17,
        'name': 'Parsnips FV0029',
        'code': 'parsnips',
        'pack_size': '500g',
        'price': Money(1.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':18,
        'name': 'Potatoes : Ambo / King Edward FV0032',
        'code': 'potatoes-ambo-edward',
        'pack_size': '1 kg',
        'price': Money(0.96,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':19,
        'name': 'Potatoes : Estima Baking FV0031',
        'code': 'potatoes-estima',
        'pack_size': '1 kg',
        'price': Money(1.45,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':20,
        'name': 'Potatoes: Salad  FV0159',
        'code': 'potatoes-salad',
        'pack_size': '1 kg',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':21,
        'name': 'Swede FV0034',
        'code': 'swede',
        'pack_size': '1',
        'price': Money(0.46,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':22,
        'name': 'Sweet Potato FV0035',
        'code': 'sweet-potato',
        'pack_size': '1',
        'price': Money(0.84,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':23,
        'name': 'Avocado : Ripe ready to eat FV0094',
        'code': 'avocado',
        'pack_size': '1',
        'price': Money(1.55,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':24,
        'name': 'Baby Leaf Salad Bag FV0225',
        'code': 'salad-bag',
        'pack_size': '1',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':25,
        'name': 'Celery FV0111',
        'code': 'celery',
        'pack_size': '1',
        'price': Money(1.1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':26,
        'name': 'Cucumber FV0118',
        'code': 'cucumber',
        'pack_size': '1',
        'price': Money(1.1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':27,
        'name': 'Lettuce  : little gem FV0179',
        'code': 'lettuce-gem',
        'pack_size': '1',
        'price': Money(1.45,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':28,
        'name': 'Lettuce :Romaine FV0137',
        'code': 'lettuce-romaine',
        'pack_size': '1',
        'price': Money(1.35,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':29,
        'name': 'Peppers : Red FV0030',
        'code': 'peppers-red',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':30,
        'name': 'Spring onions FV0169',
        'code': 'spring-onions',
        'pack_size': '1',
        'price': Money(0.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':31,
        'name': 'Tomato : classic vine FV0038',
        'code': 'tomato-vine',
        'pack_size': '500g',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':32,
        'name': 'Garlic bulb FV0000',
        'code': 'garlic-bulb',
        'pack_size': '1',
        'price': Money(1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':33,
        'name': 'Apples - Eating FV2209',
        'code': 'apples-english-eating',
        'pack_size': '1 kg',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':34,
        'name': 'Bananas : fair trade FV0002',
        'code': 'bananas-fair-trade',
        'pack_size': '500g',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':35,
        'name': 'Blueberries FV0074',
        'code': 'blueberries',
        'pack_size': '1',
        'price': Money(2.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':36,
        'name': 'Clementines / satsumas FV0003',
        'code': 'clementines-satsumas',
        'pack_size': '500g',
        'price': Money(1.65,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':37,
        'name': 'Grapefruit FV0058',
        'code': 'grapefruit',
        'pack_size': '1',
        'price': Money(0.55,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':38,
        'name': 'Grapes : Black seedless FV0004',
        'code': 'grapes-black',
        'pack_size': '500g',
        'price': Money(2.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':39,
        'name': 'Grapes : White seedless FV9000',
        'code': 'grapes-white',
        'pack_size': '500g',
        'price': Money(2.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':40,
        'name': 'Kiwi fruit FV0114',
        'code': 'kiwi',
        'pack_size': '1',
        'price': Money(0.30,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':41,
        'name': 'Lemon FV0059',
        'code': 'lemon',
        'pack_size': '1',
        'price': Money(0.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':42,
        'name': 'Lime FV0060',
        'code': 'lime',
        'pack_size': '1',
        'price': Money(0.30,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':43,
        'name': 'Oranges : Large FV0071',
        'code': 'oranges-large',
        'pack_size': '1',
        'price': Money(0.55,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':44,
        'name': 'Pear - Conference FV0005',
        'code': 'pear-conference',
        'pack_size': '1 kg',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':45,
        'name': 'Raspberries FV0063',
        'code': 'raspberries',
        'pack_size': '125g',
        'price': Money(3.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':46,
        'name': 'Strawberries FV0065',
        'code': 'strawberries',
        'pack_size': '250g',
        'price': Money(2.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':47,
        'name': '1 Pint Full Fat : Aldhurst Farm MI5020',
        'code': 'pint-aldhurst-full-fat',
        'pack_size': '1',
        'price': Money(1.10,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':48,
        'name': '1 Pint Semi Skimmed : Aldhurst Farm MI5020',
        'code': 'pint-aldhurst-semi',
        'pack_size': '1',
        'price': Money(1.10,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':49,
        'name': '2 L Full Fat MI1022',
        'code': '2l-full-fat',
        'pack_size': '1',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':50,
        'name': '1 L Full Fat MI1024',
        'code': '1l-full-fat',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':51,
        'name': '2 L Semi Skimmed MI9001',
        'code': '2l-semi',
        'pack_size': '1',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':52,
        'name': '1 L Semi Skimmed MI9002',
        'code': '1l-semi',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':53,
        'name': '1 Pint Semi Skimmed MI9008',
        'code': '1p-semi',
        'pack_size': '1',
        'price': Money(0.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':54,
        'name': '1 L Skimmed MI9003',
        'code': '1l-skimmed',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':55,
        'name': '1 Pint Skimmed MI1027',
        'code': '1p-skimmed',
        'pack_size': '1',
        'price': Money(0.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':56,
        'name': 'Chalk Hills Bloomer BR2291',
        'code': 'chalk-hills-bloomer',
        'pack_size': '1',
        'price': Money(2.1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':57,
        'name': 'Chalk Hills Large White Tin BR3599',
        'code': 'chalk-hills-white-tin',
        'pack_size': '1',
        'price': Money(2.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':58,
        'name': 'Chalk Hills Large White Sliced BR9004',
        'code': 'chalk-hills-white-sliced',
        'pack_size': '1',
        'price': Money(2.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':59,
        'name': 'Chalk Hills Large Wholemeal Tin BR3600',
        'code': 'chalk-hills-whole-tin',
        'pack_size': '1',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':60,
        'name': 'Chalk Hills Large Wholemeal Sliced BR9005',
        'code': 'chalk-hills-whole-sliced',
        'pack_size': '1',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':61,
        'name': 'Chalk Hills White Spelt BR2286',
        'code': 'chalk-hills-white-spelt',
        'pack_size': '1',
        'price': Money(2.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':62,
        'name': 'Chalk Hills Croissants x 2 BR1396',
        'code': 'chalk-hills-croissants-2',
        'pack_size': '1',
        'price': Money(2.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':63,
        'name': 'Eggs : Free Range box of 6 SZ1314',
        'code': 'eggs-free-range-6-box',
        'pack_size': '1',
        'price': Money(1.9,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':64,
        'name': 'Coffee Real Ground SZ0839',
        'code': 'coffee-real-ground',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':65,
        'name': 'Coffee Real Beans SZ9006',
        'code': 'coffee-real-beans',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':66,
        'name': 'Tea Bags : Clipper Everyday x 80 (Organic) SZ0823',
        'code': 'tea-clipper-80',
        'pack_size': '1',
        'price': Money(2.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':67,
        'name': 'Tea Bags : Clipper Everyday x 40 (Organic) SZ0821',
        'code': 'tea-clipper-40',
        'pack_size': '1',
        'price': Money(3.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':68,
        'name': 'Moores Biscuits 150g : Ginger SZ0710',
        'code': 'moores-biscuits-ginger',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':69,
        'name': "Moores Biscuits 150g : Chocolate Chip SZ2659",
        'code': 'moores-bisciots-choc-chip',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':70,
        'name': "Debbie's Seville Orange Marmalade 340g SZ0532",
        'code': 'seville-organge-marmalade',
        'pack_size': '1',
        'price': Money(4.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':71,
        'name': 'Local Honey - runny 340g SZ0541',
        'code': 'local-runny-honey',
        'pack_size': '1',
        'price': Money(7.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':72,
        'name': 'Ouse Valley Cheeseboard Chutney 300g SZ0473',
        'code': 'ouse-valley-cheeseboard',
        'pack_size': '1',
        'price': Money(5.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':73,
        'name': 'Stockans Thick Triangular Oatcakes 200g SZ0745',
        'code': 'stockands-oatcakes-200g',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':74,
        'name': 'Peters Yard Sourdough Crackers 100g SZ2765',
        'code': 'peters-yard-sourdough-crackers-100g',
        'pack_size': '1',
        'price': Money(3.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':75,
        'name': 'Tims Greek Style Yoghurt : Natural 500g SZ1198',
        'code': 'tims-yoghurt-natrual-500g',
        'pack_size': '1',
        'price': Money(2.35,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':76,
        'name': 'Tims Greek Style Yoghurt : Natural 200g SZ1201',
        'code': 'tims-yoghurt-natrual-200g',
        'pack_size': '1',
        'price': Money(1.35,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':77,
        'name': 'Double Cream 250ml SZ0240',
        'code': 'double-cream-250ml',
        'pack_size': '1',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':78,
        'name': 'Loseley Salted Butter 250g SZ1238',
        'code': 'loosely-salted-butter-250g',
        'pack_size': '1',
        'price': Money(3.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':79,
        'name': 'Sussex Charmer Cheese 200g (Vegetarian) SZ1127',
        'code': 'sussex-charmer-cheese-200g',
        'pack_size': '1',
        'price': Money(3.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':80,
        'name': 'Sussex Charmer Cheese 500g (Vegetarian) SZ3796',
        'code': 'sussex-charmer-cheese-250g',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':81,
        'name': 'Balck Bomber Cheese Truckle 200g (Vegetarian) SZ1123',
        'code': 'bomber-cheese-truckle-200g',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':82,
        'name': 'Norbury Blue Cheese approx. 150 - 200g SZ9007',
        'code': 'norbury-blue-cheese',
        'pack_size': '1 kg',
        'price': Money(32,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':83,
        'name': 'Suma Tinned Soup : Pea (Organic, Vegan) SZ4674',
        'code': 'suma-soup-pea',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':84,
        'name': 'Suma Tinned Soup : Tuscan Bean  (Organic, Vegan) SZ1322',
        'code': 'suma-soup-tuscan-bean',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':85,
        'name': 'Suma Tinned Soup : Tomato  (Organic, Vegan) SZ1320',
        'code': 'suma-soup-tomato',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':86,
        'name': 'Ecoleaf Laundry Liquid 1.5L ST4883',
        'code': 'ecoleaf-laundry-liquid',
        'pack_size': '1',
        'price': Money(7.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':87,
        'name': 'Ecoleaf Washing Up Liquid 1L ST4978',
        'code': 'ecoleaf-washingup',
        'pack_size': '1',
        'price': Money(3.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':88,
        'name': 'Ecoleaf Dishwasher Tablets x25 ST4903',
        'code': 'ecoleaf-dishwasher',
        'pack_size': '1',
        'price': Money(6.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':89,
        'name': 'Horsham Gingerbread SZ2194',
        'code': 'horsham-gingerbread',
        'pack_size': '1',
        'price': Money(3.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':90,
        'name': 'Horsham Gingerbread : Gluten Free SZ2528',
        'code': 'horsham-gingerbread-gluten-free',
        'pack_size': '1',
        'price': Money(4.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':91,
        'name': 'Monty Bojangles Choccy Scoffy Truffles 150g ST1486',
        'code': 'choccy-scoffy-truffles',
        'pack_size': '1',
        'price': Money(4.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':92,
        'name': "Montezuma's 51% Dark Side Chocolate 90g (Organic) ST1528",
        'code': 'montezumas-dark-choc-90g',
        'pack_size': '1',
        'price': Money(2.85,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':93,
        'name': 'Kent & Fraser Lemon Butter Biscuits 125g (Gluten Free) SZ0718',
        'code': 'kent-fraser-lemon',
        'pack_size': '1',
        'price': Money(3.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':94,
        'name': 'Ringden Apple Juice 1L - Cox Bramley Med Sweet ST0370',
        'code': 'ringdon-apple-juice-1l-cox-sweet',
        'pack_size': '1',
        'price': Money(2.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':95,
        'name': 'Hogs Back Tea Traditional English Ale 500ml ST0325',
        'code': 'hogs-back-tea',
        'pack_size': '1',
        'price': Money(3.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':96,
        'name': 'Shere Drop Real Ale 500g ST0306',
        'code': 'coffee-real-beans',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':97,
        'name': 'Silent Pool Gin 70cl ST3001',
        'code': 'silent-pool-gin',
        'pack_size': '1',
        'price': Money(38.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':98,
        'name': 'Dancing Dragontail Gin 70cl ST3905',
        'code': 'dragontail-gin',
        'pack_size': '1',
        'price': Money(47.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':99,
        'name': 'Fever Tree Elderflower Tonic 500ml ST3516',
        'code': 'fever-tree-500ml',
        'pack_size': '1',
        'price': Money(2.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':100,
        'name': 'Denbies Wine : Surrey Gold 70cl ST0270',
        'code': 'surrey-gold',
        'pack_size': '1',
        'price': Money(9.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':101,
        'name': 'Denbies Wine : Flint Valley 70cl ST0269',
        'code': 'denbies-wine-flint',
        'pack_size': '1',
        'price': Money(9.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':102,
        'name': 'Hepworth Sussex Ale 500ml ST0309',
        'code': 'hepworth-ale',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':103,
        'name': 'Hepworth Blonde Lager 330ml (Organic, GF, Vegan) ST0336',
        'code': 'hepworth-lager-330',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':104,
        'name': 'Hepworth Blonde Lager 500ml  (Organic, GF, Vegan) ST0327',
        'code': 'hepworth-lager-500',
        'pack_size': '1',
        'price': Money(2.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':105,
        'name': 'Chalk Hills Large Sourdough loaf SZ2649',
        'code': 'chalk-hills-large-sourdough',
        'pack_size': '1',
        'price': Money(3.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },



]
