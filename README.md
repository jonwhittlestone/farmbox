# farmbox

![Continuous Integration and Delivery](https://github.com/jonwhittlestone/farmbox/workflows/Continuous%20Integration%20and%20Delivery/badge.svg)

A Django 3 app for a more efficient workflow for food delivery organisations.

Currently supports order systems that take in orders by xlsx. It aids fulfillment by producing a generated xlsx to better enable staff to pick and pack the produce.

Example Workflow

1. The user uploads new order spreadsheets (xlsx) to the `new-orders` dropbox and initiates a `Fetch` operation in the Django Admin interface.

2. They are ingested by the system according to fulfillment event target date. - For example, if the xlsx cell has a _Deliver / Collection Date_ of 21st December 2020, the desired product quantities are read and the fulfillment event for 21/12/2020 is created.

3. Repeat orders forms do not need to be reingested from Dropbox. They can be duplicated to a new fulfillment event. See below where 3 orders are duplicated from 8th June event to 1st August event.

![](https://i.imgur.com/17kTXnT.gif)

## Secrets

Vault: Freelance Customers > Village Greens Farmbox

## Dropbox

The Django app uses a Dropbox app for storage.

u: farmbox--dev@outlook.com
dashboard: [here](https://www.dropbox.com/developers/apps/info/2x58355mwxchk2t)

## Local Development

TLDR; see [CI](.github/workflows/main.yml)

1. Create the `.env` file for local development.

```
cp .env.dev.example .env.dev
```

2. Populate the `FARMBOX_DROPBOX_ACCESS_TOKEN`

```
echo "FARMBOX_DROPBOX_ACCESS_TOKEN=changeme" >> .env.dev
```

3. Run the docker containers

```
docker-compose up
```

4. Go to http://localhost:8000 in a browser

5. [Optional] Run the Database migrations

```
docker-compose exec web python manage.py migrate
```

6. Change the password for the admin user

```
docker-compose exec web python manage.py changepassword admin
```

### Run local tests

```
docker-compose exec -T web pytest -v
```

## Release History

- 2020.07.25

  - Usage docs
  - Dev dockerfile

- 2020.11.06

  - Feature: Customer model. Created from order sheet ingestion
  - Feature: Product selection parsing from dropbox

- 2020.07.06

  - Fix: Customer sheet product headers ordering matches quantity
  - Fix: Parsing all words in last name is Sentence Case

- 2020.06.26

  - Restore db backup
  - Product sequence editing with adminsortable2 widget

- 2020.06.23
  - Customer order form parsing from Dropbox
  - Customer sheet generation (PDF/XLSX)
  - Static product selection #0 (< June 2020)
  - Duplicate order to new event as repeat

## Current Limitations

- Created repeat order forms do not currently take into account unpublished products

## What's next ..

```
==========================================
Phase 1
==========================================
[x] Creating the order from the sheet
[x] Plumbing in header metrics and tidy up
[x] Order spreadsheets ingestion from dropbox
[x] New product selection / May order form
[x] Deployment
[x] Customer sheets generation
[x] Duplicate order to a new Fulfillment Event
[ ] Receipts
        [ ] Invoice/Costing calculation
[x] Dynamic Product listing


## Bugs
- cleanup of /mediafiles if there is an uncaught reader exception

==========================================
Phase 2
==========================================
[ ] User groups
[ ] Multi-tenancy
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

## To start project yourself, you'll need:

- Access to the linked dropbox account

- To save new order forms to the following dropbox folder: - ![dropbox](dropbox.png)

## API

Prerequisites

- Python==3.8
- Environment variables:

        export FARMBOX_DROPBOX_ACCESS_TOKEN=CHANGEME
        export DEFAULT_SUPERUSER_EMAIL=CHANGEME
        DEFAULT_SUPERUSER_PASSWORD=CHANGEME
        export DEFAULT_SUPERUSER_PASSWORD=CHANGEME
        DEBUG=1
        DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'

### Quickstart

1.  Clone this repo
2.  `cd api`
3.  With the virtual environment activated, install the API dependencies
    pip install -r requirements.txt
4.  Run the migrations

        ./manage.py migrate

5.  Run the development server

        api $ ./manage.py runserver

6.  Log in at with the default superuser credentials (admin/Evoke-Enduring8-Figurine):

        http://localhost:8000/admin/

7.  There are a few tests scattered around.

        (venv) ➜  api git:(master) ✗ ../venv/bin/pytest .
        ============================================================== test session starts ==============================================================
        platform linux -- Python 3.8.0, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
        django: settings: farmbox.settings (from ini)
        rootdir: /home/jon/code/playground/farmbox/api, inifile: pytest.ini
        plugins: factoryboy-2.0.3, django-3.9.0
        collected 7 items

        order/tests.py .......                                                                                                                    [100%]

        =============================================================== 7 passed in 0.94s ===============================================================
