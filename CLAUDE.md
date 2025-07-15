# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 3.0.7 web application for managing food delivery orders. The system ingests order spreadsheets from Dropbox, processes them, and generates customer sheets for fulfillment.

## Key Commands

### Development
```bash
# Run tests
pytest api -v
pytest api/order/tests/test_views.py -v  # Run specific test file

# Start development server
./manage.py runserver

# Database operations
./manage.py migrate
./manage.py makemigrations
./manage.py show_db_snapshot  # Show database contents

# Django shell
./manage.py shell_plus

# Create superuser
./manage.py createsuperuser
```

### Docker Development
```bash
# Start development environment
docker-compose up

# Production deployment
docker-compose -f docker-compose.prod.yml up
```

## Architecture Overview

### Core Django Apps
- **order**: Central app managing fulfillment events and orders
- **customer**: Customer management and tracking
- **product**: Product catalog with dynamic selection
- **sheets**: Excel/PDF generation for customer fulfillment sheets
- **cloudstore**: Dropbox integration for file storage
- **snapshot**: Database backup/restore functionality

### Key Models and Relationships
- `FulfillmentEvent` → `Order` → `Customer`
- `Order` → `OrderProduct` ← `Product`
- Orders are imported from Excel sheets uploaded to Dropbox
- Customer sheets are generated as PDF/Excel for fulfillment

### Important Files
- `api/order/views.py`: Main order processing logic
- `api/sheets/generators/`: Customer sheet generation (PDF/Excel)
- `api/cloudstore/gateway.py`: Dropbox integration
- `api/farmbox/settings.py`: Django configuration

### Testing Approach
- Uses pytest with pytest-django
- Test files follow pattern: `test_*.py`
- Fixtures in `conftest.py` files
- Run with `pytest api -v`

### Environment Variables
Required for operation:
- `FARMBOX_DROPBOX_ACCESS_TOKEN`
- `DEFAULT_SUPERUSER_EMAIL`
- `DEFAULT_SUPERUSER_PASSWORD`
- `DEBUG` (True/False)
- `DJANGO_ALLOWED_HOSTS`

### Key Workflows
1. **Order Import**: Upload XLSX to Django Admin → Process into Orders
2. **Sheet Generation**: Select orders → Generate PDF/Excel sheets
3. **Repeat Orders**: Duplicate orders to new fulfillment events
4. **Product Management**: Update product catalog and pricing

### API Endpoints
- GraphQL endpoint at `/graphql/`
- Django Admin at `/admin/`
- Customer sheets download at `/customer-sheets/<id>/`