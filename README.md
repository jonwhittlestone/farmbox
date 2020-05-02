# farmbox

A Django 3 app for better workflow for farm shops that take in orders by xlsx. Currently, it aids fulfillment by producing a generated xlsx to better enable staff to pick and pack the produce.

This repo is to contain code for both `api` and `client`

![admin](screenshot.png)

## Current Limitations
- Fixed product listing

- Fixed XLSX order form (see [order/sample-order-v070420.xlsx](order/sample-order-v070420.xlsx))

- No separate customer model. Cannot see all historical orders for a single customer

## What's next ..
```
==========================================
Phase 1
==========================================
[x] Creating the order from the sheet
[x] Plumbing in header metrics and tidy up
[ ] Order spreadsheets ingestion from cloud storage
[ ] Getting it on the web: Dockerizing / github actions deployment
        - SECRETS/env_vars
[ ] Bug tracking/analytics
        - Sentry
        - GA
[ ] Customer/Receipt sheets generation
        - Order number system
        - Use in actual VG operation!
[ ] Invoice/Costing calculation

## Bugs
- no registration/login.html template for deeplink/?next 

==========================================
Phase 2
==========================================
[ ] Web Order Form
[ ] Stripe integration
        [ ] Delivery management
        [ ] Customer Collection management
        [ ] Separate customer model
        [ ] State Machine
        [ ] Order form generation from product model

==========================================
Phase 3
==========================================
[ ] Mobile app for picking management / updating order
```

## API

Prerequisites

* Python==3.6  (for Microsoft Graph SDK)

Quickstart

1. Clone this repo
2. `cd api`
3. With the virtual environment activated, install the API dependencies

        pip install -r requirements.txt
4. Run the migrations

        ./manage.py migrate
3. Run the development server

        api $ ./manage.py runserver

4. Log in at with the default superuser credentials (admin/Evoke-Enduring8-Figurine):

        http://localhost:8000/admin/

5. There are a few tests scattered around.
        
        (venv) ➜  api git:(master) ✗ ../venv/bin/pytest order/tests.py
        ============================================================== test session starts ==============================================================
        platform linux -- Python 3.8.0, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
        django: settings: farmbox.settings (from ini)
        rootdir: /home/jon/code/playground/farmbox/api, inifile: pytest.ini
        plugins: factoryboy-2.0.3, django-3.9.0
        collected 7 items                                                                                                                               

        order/tests.py .......                                                                                                                    [100%]

        =============================================================== 7 passed in 0.94s ===============================================================
        
