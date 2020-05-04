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
        'name': 'Fine green beans',
        'slug': 'fine-green-beans',
        'pack_size': '250g',
        'price': Money(2.5, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':4,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Broccoli',
        'slug': 'broccoli',
        'pack_size': 'Head appr 250g',
        'price': Money(2.5, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':5,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Butternut Squash',
        'slug': 'butternut-squash',
        'pack_size': '1',
        'price': Money(1, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':6,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'name': 'Cabbage Hispi',
        'slug': 'cabbage-hispi',
        'pack_size': '1',
        'price': Money(1.3, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':7,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'name': 'Cabbage Savoy',
        'slug': 'cabbage-savoy',
        'pack_size': '1',
        'price': Money(1.95, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':8,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Cabbage Red',
        'slug': 'cabbage-red',
        'pack_size': '1',
        'price': Money(1.3, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':9,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Carrots : loose washed',
        'slug': 'carrots-loose',
        'pack_size': '500g',
        'price': Money(0.8, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':10,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Cauliflower',
        'slug': 'cauliflower',
        'pack_size': '1',
        'price': Money(3.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':11,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Courgette',
        'slug': 'courgette',
        'pack_size': '1',
        'price': Money(1.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':12,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':13,
        'name': 'Leeks',
        'slug': 'leeks',
        'pack_size': '500g',
        'price': Money(1.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':14,
        'name': 'Mushroom Cup',
        'slug': 'mushroom-cup',
        'pack_size': '150g',
        'price': Money(0.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':15,
        'name': 'Onions',
        'slug': 'onions',
        'pack_size': '500g',
        'price': Money(0.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':16,
        'name': 'Parsnips',
        'slug': 'parsnips',
        'pack_size': '500g',
        'price': Money(1.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':17,
        'name': 'Potatoes : Ambo / King Edward',
        'slug': 'potatoes-ambo-edward',
        'pack_size': '1 kg',
        'price': Money(1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':18,
        'name': 'Potatoes : Estima Baking',
        'slug': 'potatoes-estima',
        'pack_size': '1 kg',
        'price': Money(1.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':19,
        'name': 'Potatoes: Salad',
        'slug': 'potatoes-salad',
        'pack_size': '1 kg',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':20,
        'name': 'Swede',
        'slug': 'swede',
        'pack_size': '1',
        'price': Money(0.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':21,
        'name': 'Sweet Potato',
        'slug': 'sweet-potato',
        'pack_size': '1',
        'price': Money(1.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':22,
        'name': 'Avocado : Ripe ready to eat',
        'slug': 'avocado',
        'pack_size': '1',
        'price': Money(1.85,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':23,
        'name': 'Baby Leaf Salad Bag',
        'slug': 'salad-bag',
        'pack_size': '1',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':24,
        'name': 'Celery',
        'slug': 'celery',
        'pack_size': '1',
        'price': Money(1.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':25,
        'name': 'Cucumber',
        'slug': 'cucumber',
        'pack_size': '1',
        'price': Money(1.1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':26,
        'name': 'Lettuce  : little gem',
        'slug': 'lettuce-gem',
        'pack_size': '1',
        'price': Money(1.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':27,
        'name': 'Lettuce :Romaine',
        'slug': 'lettuce-gem',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':28,
        'name': 'Peppers : Red',
        'slug': 'peppers-red',
        'pack_size': '1',
        'price': Money(1.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':29,
        'name': 'Spring onions',
        'slug': 'spring-onions',
        'pack_size': '1',
        'price': Money(0.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':30,
        'name': 'Tomato : classic vine',
        'slug': 'tomato-vine',
        'pack_size': '500g',
        'price': Money(0.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':31,
        'name': 'Apples - English Eating',
        'slug': 'apples-english-eating',
        'pack_size': '1 kg',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':32,
        'name': 'Bananas : fair trade',
        'slug': 'bananas-fair-trade',
        'pack_size': '500g',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':33,
        'name': 'Blueberries',
        'slug': 'blueberries',
        'pack_size': '1',
        'price': Money(2.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':34,
        'name': 'Clementines / satsumas',
        'slug': 'clementines-satsumas',
        'pack_size': '500g',
        'price': Money(1.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':35,
        'name': 'Grapefruit',
        'slug': 'grapefruit',
        'pack_size': '1',
        'price': Money(0.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':36,
        'name': 'Grapes : Black seedless',
        'slug': 'grapes-black',
        'pack_size': '500g',
        'price': Money(3.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':37,
        'name': 'Grapes : White seedless',
        'slug': 'grapes-white',
        'pack_size': '500g',
        'price': Money(3.5,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':38,
        'name': 'Kiwi fruit',
        'slug': 'kiwi',
        'pack_size': '1',
        'price': Money(0.35,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':39,
        'name': 'Lemon',
        'slug': 'lemon',
        'pack_size': '1',
        'price': Money(0.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':40,
        'name': 'Lime',
        'slug': 'lime',
        'pack_size': '1',
        'price': Money(0.35,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':41,
        'name': 'Oranges : Large',
        'slug': 'oranges-large',
        'pack_size': '1',
        'price': Money(0.65,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':42,
        'name': 'Pear - Conference',
        'slug': 'pear-conference',
        'pack_size': '1 kg',
        'price': Money(0.65,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':43,
        'name': 'Raspberries',
        'slug': 'raspberries',
        'pack_size': '125g',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':44,
        'name': 'Strawberries',
        'slug': 'strawberries',
        'pack_size': '250g',
        'price': Money(1.95,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':45,
        'name': '1 pint Aldhurst Farm Glass bottles : Full Fat',
        'slug': 'pint-aldhurst-full-fat',
        'pack_size': '1',
        'price': Money(1.10,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':46,
        'name': '1 pint Aldhurst Farm Glass bottles : Semi Skimmed',
        'slug': 'pint-aldhurst-semi',
        'pack_size': '1',
        'price': Money(1.10,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':47,
        'name': '2 L Full Fat',
        'slug': '2l-full-fat',
        'pack_size': '1',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':48,
        'name': '1 L Full Fat',
        'slug': '1l-full-fat',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':49,
        'name': '2 L Semi Skimmed',
        'slug': '2l-semi',
        'pack_size': '1',
        'price': Money(2.25,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':50,
        'name': '1 L Semi Skimmed',
        'slug': '1l-semi',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':51,
        'name': '1 Pint Semi Skimmed',
        'slug': '1p-semi',
        'pack_size': '1',
        'price': Money(0.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':52,
        'name': '1 L Skimmed',
        'slug': '1l-skimmed',
        'pack_size': '1',
        'price': Money(1.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':53,
        'name': '1 Pint Skimmed',
        'slug': '1p-skimmed',
        'pack_size': '1',
        'price': Money(0.8,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':54,
        'name': 'Chalk Hills Bloomer',
        'slug': 'chalk-hills-bloomer',
        'pack_size': '1',
        'price': Money(2.1,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':55,
        'name': 'Chalk Hills Large White Tin',
        'slug': 'chalk-hills-white-tin',
        'pack_size': '1',
        'price': Money(2.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':56,
        'name': 'Chalk Hills Large White Sliced',
        'slug': 'chalk-hills-white-sliced',
        'pack_size': '1',
        'price': Money(2.3,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':57,
        'name': 'Chalk Hills Large Wholemeal Tin',
        'slug': 'chalk-hills-whole-tin',
        'pack_size': '1',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':58,
        'name': 'Chalk Hills Large Wholemeal Sliced',
        'slug': 'chalk-hills-whole-sliced',
        'pack_size': '1',
        'price': Money(2.4,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'sequence':59,
        'name': 'Chalk Hills White Spelt',
        'slug': 'chalk-hills-white-spelt',
        'pack_size': '1',
        'price': Money(2.75,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':60,
        'name': 'Chalk Hills Croissants x 2',
        'slug': 'chalk-hills-croissants-2',
        'pack_size': '1',
        'price': Money(2.6,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':61,
        'name': 'Eggs : Free Range box of 6',
        'slug': 'eggs-free-range-6-box',
        'pack_size': '1',
        'price': Money(1.9,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':62,
        'name': 'Coffee Real Ground',
        'slug': 'coffee-real-ground',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'sequence':63,
        'name': 'Coffee Real Beans',
        'slug': 'coffee-real-beans',
        'pack_size': '1',
        'price': Money(6.15,settings.DEFAULT_CURRENCY),
        'published': True,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },



]
