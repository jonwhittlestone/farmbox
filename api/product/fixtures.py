from django.conf import settings
from djmoney.money import Money

initial_products = [
    {
        'name': 'Village Greens Veg Bag : Large',
        'slug': 'village-greens-veg-bag-large',
        'pack_size': '9-10 lines',
        'price': Money(15, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':1,
        'category': settings.PRODUCT_CATEGORIES_VEGBAG,
    },

    {
        'name': 'Village Greens Veg Bag : Medium',
        'slug': 'village-greens-veg-bag-medium',
        'pack_size': '8-9 lines',
        'price': Money(13, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':2,
        'category': settings.PRODUCT_CATEGORIES_VEGBAG
    },
    {
        'name': 'Village Greens Veg Bag : Small',
        'slug': 'village-greens-veg-bag-small',
        'pack_size': '7-8 lines',
        'price': Money(11, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':3,
        'category': settings.PRODUCT_CATEGORIES_VEGBAG
    },
    {
        'name': 'Asparagus',
        'slug': 'asparagus',
        'pack_size': '250g',
        'price': Money(2.95, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':4,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Fine green beans',
        'slug': 'fine-green-beans',
        'pack_size': '250g',
        'price': Money(2.45, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':5,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Broccoli',
        'slug': 'broccoli',
        'pack_size': 'Head appr 400g',
        'price': Money(1.25, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':6,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Butternut Squash',
        'slug': 'butternut-squash',
        'pack_size': '1',
        'price': Money(1.35, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':7,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'name': 'Cabbage Hispi',
        'slug': 'cabbage-hispi',
        'pack_size': '1',
        'price': Money(1.8, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':8,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'name': 'Cabbage Savoy',
        'slug': 'cabbage-savoy',
        'pack_size': '1',
        'price': Money(2.75, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':9,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Cabbage Red',
        'slug': 'cabbage-red',
        'pack_size': '1',
        'price': Money(0.7, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':10,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Carrots : loose washed',
        'slug': 'carrots-loose',
        'pack_size': '500g',
        'price': Money(0.6, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':11,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Cauliflower',
        'slug': 'cauliflower',
        'pack_size': '1',
        'price': Money(3.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':12,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Courgette',
        'slug': 'courgette',
        'pack_size': '500g',
        'price': Money(1.28,settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':13,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':14,
        'name': 'Leeks',
        'slug': 'leeks',
        'pack_size': '500g',
        'price': Money(1.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':15,
        'name': 'Mushroom Cup',
        'slug': 'mushroom-cup',
        'pack_size': '150g',
        'price': Money(0.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':16,
        'name': 'Onions',
        'slug': 'onions',
        'pack_size': '500g',
        'price': Money(0.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':17,
        'name': 'Parsnips',
        'slug': 'parsnips',
        'pack_size': '500g',
        'price': Money(1.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':18,
        'name': 'Potatoes : Ambo / King Edward',
        'slug': 'potatoes-ambo-edward',
        'pack_size': '1 kg',
        'price': Money(0.96,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':19,
        'name': 'Potatoes : Estima Baking',
        'slug': 'potatoes-estima',
        'pack_size': '1 kg',
        'price': Money(1.45,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':20,
        'name': 'Potatoes: Salad',
        'slug': 'potatoes-salad',
        'pack_size': '1 kg',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':21,
        'name': 'Swede',
        'slug': 'swede',
        'pack_size': '1',
        'price': Money(0.46,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':22,
        'name': 'Sweet Potato',
        'slug': 'sweet-potato',
        'pack_size': '1',
        'price': Money(0.84,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':23,
        'name': 'Avocado : Ripe ready to eat',
        'slug': 'avocado',
        'pack_size': '1',
        'price': Money(1.55,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':24,
        'name': 'Baby Leaf Salad Bag',
        'slug': 'salad-bag',
        'pack_size': '1',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':25,
        'name': 'Celery',
        'slug': 'celery',
        'pack_size': '1',
        'price': Money(1.1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':26,
        'name': 'Cucumber',
        'slug': 'cucumber',
        'pack_size': '1',
        'price': Money(1.1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':27,
        'name': 'Lettuce  : little gem',
        'slug': 'lettuce-gem',
        'pack_size': '1',
        'price': Money(1.45,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':28,
        'name': 'Lettuce :Romaine',
        'slug': 'lettuce-gem',
        'pack_size': '1',
        'price': Money(1.35,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':29,
        'name': 'Peppers : Red',
        'slug': 'peppers-red',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':30,
        'name': 'Spring onions',
        'slug': 'spring-onions',
        'pack_size': '1',
        'price': Money(0.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':31,
        'name': 'Tomato : classic vine',
        'slug': 'tomato-vine',
        'pack_size': '500g',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':32,
        'name': 'Garlic bulb',
        'slug': 'garlic-bulb',
        'pack_size': '1',
        'price': Money(1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':33,
        'name': 'Apples - English Eating',
        'slug': 'apples-english-eating',
        'pack_size': '1 kg',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':34,
        'name': 'Bananas : fair trade',
        'slug': 'bananas-fair-trade',
        'pack_size': '500g',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':35,
        'name': 'Blueberries',
        'slug': 'blueberries',
        'pack_size': '1',
        'price': Money(2.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':36,
        'name': 'Clementines / satsumas',
        'slug': 'clementines-satsumas',
        'pack_size': '500g',
        'price': Money(1.65,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':37,
        'name': 'Grapefruit',
        'slug': 'grapefruit',
        'pack_size': '1',
        'price': Money(0.55,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':38,
        'name': 'Grapes : Black seedless',
        'slug': 'grapes-black',
        'pack_size': '500g',
        'price': Money(2.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':39,
        'name': 'Grapes : White seedless',
        'slug': 'grapes-white',
        'pack_size': '500g',
        'price': Money(2.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':40,
        'name': 'Kiwi fruit',
        'slug': 'kiwi',
        'pack_size': '1',
        'price': Money(0.30,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':41,
        'name': 'Lemon',
        'slug': 'lemon',
        'pack_size': '1',
        'price': Money(0.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':42,
        'name': 'Lime',
        'slug': 'lime',
        'pack_size': '1',
        'price': Money(0.30,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':43,
        'name': 'Oranges : Large',
        'slug': 'oranges-large',
        'pack_size': '1',
        'price': Money(0.55,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':44,
        'name': 'Pear - Conference',
        'slug': 'pear-conference',
        'pack_size': '1 kg',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':45,
        'name': 'Raspberries',
        'slug': 'raspberries',
        'pack_size': '125g',
        'price': Money(3.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':46,
        'name': 'Strawberries',
        'slug': 'strawberries',
        'pack_size': '250g',
        'price': Money(2.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':47,
        'name': '1 pint Aldhurst Farm Glass bottles : Full Fat',
        'slug': 'pint-aldhurst-full-fat',
        'pack_size': '1',
        'price': Money(1.10,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':48,
        'name': '1 pint Aldhurst Farm Glass bottles : Semi Skimmed',
        'slug': 'pint-aldhurst-semi',
        'pack_size': '1',
        'price': Money(1.10,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':49,
        'name': '2 L Full Fat',
        'slug': '2l-full-fat',
        'pack_size': '1',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':50,
        'name': '1 L Full Fat',
        'slug': '1l-full-fat',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':51,
        'name': '2 L Semi Skimmed',
        'slug': '2l-semi',
        'pack_size': '1',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':52,
        'name': '1 L Semi Skimmed',
        'slug': '1l-semi',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':53,
        'name': '1 Pint Semi Skimmed',
        'slug': '1p-semi',
        'pack_size': '1',
        'price': Money(0.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':54,
        'name': '1 L Skimmed',
        'slug': '1l-skimmed',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':55,
        'name': '1 Pint Skimmed',
        'slug': '1p-skimmed',
        'pack_size': '1',
        'price': Money(0.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':56,
        'name': 'Chalk Hills Bloomer',
        'slug': 'chalk-hills-bloomer',
        'pack_size': '1',
        'price': Money(2.1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':57,
        'name': 'Chalk Hills Large White Tin',
        'slug': 'chalk-hills-white-tin',
        'pack_size': '1',
        'price': Money(2.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':58,
        'name': 'Chalk Hills Large White Sliced',
        'slug': 'chalk-hills-white-sliced',
        'pack_size': '1',
        'price': Money(2.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':59,
        'name': 'Chalk Hills Large Wholemeal Tin',
        'slug': 'chalk-hills-whole-tin',
        'pack_size': '1',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':60,
        'name': 'Chalk Hills Large Wholemeal Sliced',
        'slug': 'chalk-hills-whole-sliced',
        'pack_size': '1',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':61,
        'name': 'Chalk Hills White Spelt',
        'slug': 'chalk-hills-white-spelt',
        'pack_size': '1',
        'price': Money(2.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':62,
        'name': 'Chalk Hills Croissants x 2',
        'slug': 'chalk-hills-croissants-2',
        'pack_size': '1',
        'price': Money(2.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':63,
        'name': 'Eggs : Free Range box of 6',
        'slug': 'eggs-free-range-6-box',
        'pack_size': '1',
        'price': Money(1.9,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':64,
        'name': 'Coffee Real Ground',
        'slug': 'coffee-real-ground',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':65,
        'name': 'Coffee Real Beans',
        'slug': 'coffee-real-beans',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':66,
        'name': 'Tea Bags : Clipper Everyday x 80 (Organic)',
        'slug': 'tea-clipper-80',
        'pack_size': '1',
        'price': Money(2.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':67,
        'name': 'Tea Bags : Clipper Everyday x 40 (Organic)',
        'slug': 'tea-clipper-40',
        'pack_size': '1',
        'price': Money(3.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':68,
        'name': 'Moores Biscuits 150g : Ginger',
        'slug': 'moores-biscuits-ginger',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':69,
        'name': 'Moores Biscuits 150g : Chocolate Chip',
        'slug': 'moores-bisciots-choc-chip',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':70,
        'name': 'Debbies Seville Orange Marmalade 340g',
        'slug': 'seville-organge-marmalade',
        'pack_size': '1',
        'price': Money(4.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':71,
        'name': 'Local Honey - runny 400g',
        'slug': 'local-runny-honey',
        'pack_size': '1',
        'price': Money(7.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':72,
        'name': 'Ouse Valley Cheeseboard Chutney 300g',
        'slug': 'ouse-valley-cheeseboard',
        'pack_size': '1',
        'price': Money(5.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':73,
        'name': 'Stockans Thick Triangular Oatcakes 200g',
        'slug': 'stockands-oatcakes-200g',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':74,
        'name': 'Peters Yard Sourdough Crackers 100g',
        'slug': 'peters-yard-sourdough-crackers-100g',
        'pack_size': '1',
        'price': Money(3.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':75,
        'name': 'Tims Greek Style Yoghurt : Natural 500g',
        'slug': 'tims-yoghurt-natrual-500g',
        'pack_size': '1',
        'price': Money(2.35,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':76,
        'name': 'Tims Greek Style Yoghurt : Natural 200g',
        'slug': 'tims-yoghurt-natrual-200g',
        'pack_size': '1',
        'price': Money(1.35,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':77,
        'name': 'Double Cream 250ml',
        'slug': 'double-cream-250ml',
        'pack_size': '1',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':78,
        'name': 'Losely Salted Butter 250g',
        'slug': 'loosely-salted-butter-250g',
        'pack_size': '1',
        'price': Money(3.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':79,
        'name': 'Sussex Charmer Cheese 200g (Vegetarian)',
        'slug': 'sussex-charmer-cheese-200g',
        'pack_size': '1',
        'price': Money(3.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':80,
        'name': 'Sussex Charmer Cheese 500g (Vegetarian)',
        'slug': 'sussex-charmer-cheese-250g',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':81,
        'name': 'Balck Bomber Cheese Truckle 200g (Vegetarian)',
        'slug': 'bomber-cheese-truckle-200g',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':82,
        'name': 'Norbury Blue Cheese approx 150 - 200g',
        'slug': 'norbury-blue-cheese',
        'pack_size': '1 kg',
        'price': Money(32,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':83,
        'name': 'Suma Tinned Soup : Pea (Organic, Vegan)',
        'slug': 'suma-soup-pea',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':84,
        'name': 'Suma Tinned Soup : Tuscan Bean  (Organic, Vegan)',
        'slug': 'suma-soup-tuscan-bean',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':85,
        'name': 'Suma Tinned Soup : Tomato  (Organic, Vegan)',
        'slug': 'suma-soup-tomato',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':86,
        'name': 'Ecoleaf Laundry Liquid 1.5L',
        'slug': 'ecoleaf-laundry-liquid',
        'pack_size': '1',
        'price': Money(7.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':87,
        'name': 'Ecoleaf Washing Up Liquid 1L',
        'slug': 'ecoleaf-washingup',
        'pack_size': '1',
        'price': Money(3.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':88,
        'name': 'Ecoleaf Dishwasher Tablets x25',
        'slug': 'ecoleaf-dishwasher',
        'pack_size': '1',
        'price': Money(6.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':89,
        'name': 'Horsham Gingerbread',
        'slug': 'horsham-gingerbread',
        'pack_size': '1',
        'price': Money(3.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':90,
        'name': 'Horsham Gingerbread : Gluten Free',
        'slug': 'horsham-gingerbread-gluten-free',
        'pack_size': '1',
        'price': Money(4.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':91,
        'name': 'Monty Bojangles Choccy Scoffy Truffles 150g',
        'slug': 'choccy-scoffy-truffles',
        'pack_size': '1',
        'price': Money(4.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':92,
        'name': 'Montezumas 51% Dark Side Chocolate 90g (Organic)',
        'slug': 'montezumas-dark-choc-90g',
        'pack_size': '1',
        'price': Money(2.85,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':93,
        'name': 'Kent & Fraser Lemon Butter Biscuits 125g (Gluten Free)',
        'slug': 'kent-fraser-lemon',
        'pack_size': '1',
        'price': Money(3.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':94,
        'name': 'Ringdon Apple Juice 1L - Cox Bramley Med Sweet',
        'slug': 'ringdon-apple-juice-1l-cox-sweet',
        'pack_size': '1',
        'price': Money(2.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':95,
        'name': 'Hogs Back Tea Traditional English Ale 500ml',
        'slug': 'hogs-back-tea',
        'pack_size': '1',
        'price': Money(3.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':96,
        'name': 'Shere Drop Real Ale 500g',
        'slug': 'coffee-real-beans',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':97,
        'name': 'Silent Pool Gin 70cl',
        'slug': 'silent-pool-gin',
        'pack_size': '1',
        'price': Money(38.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':98,
        'name': 'Dancing Dragontail Gin 70cl',
        'slug': 'dragontail-gin',
        'pack_size': '1',
        'price': Money(47.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':99,
        'name': 'Fever Tree Elderflower Tonic 500ml',
        'slug': 'fever-tree-500ml',
        'pack_size': '1',
        'price': Money(2.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':100,
        'name': 'Denbies Wine : Surrey Gold 70cl',
        'slug': 'surrey-gold',
        'pack_size': '1',
        'price': Money(9.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':101,
        'name': 'Denbies Wine : Flint Valley 70cl',
        'slug': 'denbies-wine-flint',
        'pack_size': '1',
        'price': Money(9.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':102,
        'name': 'Hepworth Sussex Ale 500ml',
        'slug': 'hepworth-ale',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':103,
        'name': 'Hepworth Blonde Lager 330ml (Organic, GF, Vegan)',
        'slug': 'hepworth-lager-330',
        'pack_size': '1',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':104,
        'name': 'Hepworth Blonde Lager 500ml  (Organic, GF, Vegan)',
        'slug': 'hepworth-lager-500',
        'pack_size': '1',
        'price': Money(2.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':105,
        'name': 'Chalk Hills Large Sourdough loaf',
        'slug': 'chalk-hills-large-sourdough',
        'pack_size': '1',
        'price': Money(3.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },



]
