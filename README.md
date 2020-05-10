# farmbox

![Continuous Integration and Delivery](https://github.com/jonwhittlestone/farmbox/workflows/Continuous%20Integration%20and%20Delivery/badge.svg)

A Django 3 app for better workflow for farm shops that take in orders by xlsx. Currently, it aids fulfillment by producing a generated xlsx to better enable staff to pick and pack the produce.

The user uploads new order spreadsheets (xlsx) to the `new-orders` dropbox and initiates a `Fetch` operation in the Django Admin interface. They are ingested by the system according to fulfillment event target date. For example, if the xlsx cell has a _Deliver / Collection Date_ of 21st December 2020, the desired product quantities are read and the fulfillment event for 21/12/2020 is created.

This code repository can contain code for both `api` and `client`

![admin](screenshot.png)

## For use, you will need:

* Access to the linked dropbox account

* To save new order forms to the following dropbox folder:
        - ![dropbox](dropbox.png)

## Current Limitations
- Fixed product listing

- Fixed XLSX order form (see [api/order/sample_sheets/current.xlsx](api/order/sample_sheets/current.xlsx))

- No separate customer model. Cannot see all historical orders for a single customer

## What's next ..
```
==========================================
Phase 1
==========================================
[x] Creating the order from the sheet
[x] Plumbing in header metrics and tidy up
[x] Order spreadsheets ingestion from dropbox
[x] New product selection / May order form
[ ] Deployment
        - Rebuild docker container needs to pull live sqlite DB and then reinclude
        - Fabric: Retrieve live version of database to local
[ ] Dev Quality Tools
        - Sentry: bug tracking
        - interrogate: docstring coverage
        - mypi: type checking

[x] Updated order sheet 02/05/19
[ ] Customer/Receipt sheets generation
        - Order number system
        - Use in actual VG operation!
[ ] Invoice/Costing calculation
[ ] Repeat orders

## Bugs
- validation if no products are selected
- cleanup of /mediafiles if there is an uncaught reader exception
- fulfillment target date validation if in past

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

---
## API

Prerequisites

* Python==3.8
* Environment variables:

        export FARMBOX_DROPBOX_ACCESS_TOKEN=CHANGEME
        export DEFAULT_SUPERUSER_EMAIL=CHANGEME
        DEFAULT_SUPERUSER_PASSWORD=CHANGEME
        export DEFAULT_SUPERUSER_PASSWORD=CHANGEME
        DEBUG=1
        DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'

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

        (venv) ➜  api git:(master) ✗ ../venv/bin/pytest .
        ============================================================== test session starts ==============================================================
        platform linux -- Python 3.8.0, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
        django: settings: farmbox.settings (from ini)
        rootdir: /home/jon/code/playground/farmbox/api, inifile: pytest.ini
        plugins: factoryboy-2.0.3, django-3.9.0
        collected 7 items

        order/tests.py .......                                                                                                                    [100%]

        =============================================================== 7 passed in 0.94s ===============================================================
