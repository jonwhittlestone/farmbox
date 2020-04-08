# farmbox

This repo contains code for both `api` and `client`

## API

Prerequisites

* Python3 virtual environment

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
---
## Operation - Customer Questions

15-20 bags is fine, no need for an ecommerce solution
no automated stock solution, so no checking of inventory

#### What are the basic steps from a customer making an order to a customer opening their package at home?

afdf

---
#### What is the most time-consuming step? What step do you feel is the most inefficient?
- george (she) copies from excel to master sheet
- master sheet is then costed
- 'A butternut quash is a £1'
ourdering via excel

- generate a sheet for each customer, print all out (100 sheets)
- generate picking list
- generate orders at the same time
- 

sdfgsdf

---
#### Can you categorise the products? Eg. Veg boxes, bought products

sdfgsd

---
#### Would a grand total order summary help? Split into the two delivery sites?

sdfgsd

---
#### How is the volunteer delivery managed? 

sdfgsdosort list 
sort list by postcode
6-8 to orders
when drivers come, print out individual list
customers don't provide postcodes


---
#### How many deliveries need to be done on average, and how long do they take? 

sdo6-8ofgsd
6-8, £50 per day
20% discount

---
#### Do you have any ideas for automation?

sdfgsd
going from input sheet (customer) to creating individual customer sheet

---
#### Do you have any ideas for automation in short-term?

sdfgsdo
Biggest Problem is - Where are we?? Can we do this order?

---
#### What would your ideal ordering system look like?

sdfgsdo
Customer click on website
Review confirmation then and there
Quote in advance

Pay in advance
Limit the demand. The customer would know if it could fulfillled



---
## Phase One

* Produce summary totals for a `DeliverySession` for each site as a downloadable report so client knows what goods to purchase.
* The totals are calculated by ingesting a zip containing XLSXs

## Phase Two

* Fulfillment: For each `Customer` in the `DeliverySession`, a packing list generated
* also be used as receipt. 
* Can be filtered by by `DeliverySite` and customer delivery address postcode

## Phase Three

* System awareness of products with prices, and orders
* Client pays for VPS eg £20 p/m
* Simple reporting with metabase

## Phase Four

* Email ingestion from Inbox

## Phase Four

* Customer ordering via an online form accessing own login area

## Phase Five

* Full backend and custom storefront with CC processing w/Stripe or similar
