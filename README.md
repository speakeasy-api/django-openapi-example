<div align="center">

<a href="[Speakeasy](https://speakeasyapi.dev/)">
  <img src="https://github.com/speakeasy-api/speakeasy/assets/68016351/e959f81a-b250-4003-8c5c-a45b9463fc95" alt="Speakeasy Logo" width="400">
<h2>Speakeasy Django OpenAPI Example</h2>
</a>

</div>

This example Django app demonstrates Speakeasy-recommended practices for generating clear OpenAPI specifications and SDKs.

This project was bootstrapped with Django:

```bash
django-admin openapi-django books_project
```

## Prerequisites

The only pre-requisite needed is a supported version of Python installed, we recommend a version greater than 3.8.

If you intend to generate an SDK, you'll need the Speakeasy CLI installed, or use the Speakeasy dashboard.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ritza-co/openapi-django.git
```

2. Navigate into the directory:

```bash
cd openapi-django
```

3. Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Running the application

1. Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Start the development server:

```bash
python manage.py runserver
```

### Working with the OpenAPI specification

1. [Install Speakeasy CLI](https://github.com/speakeasy-api/speakeasy#installation) on Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/speakeasy-api/speakeasy/main/install.sh | sh
```

2. To generate the OpenAPI specification file in YAML format, run:

```bash
./manage.py spectacular --file schema.yaml
```

3. To generate an SDK, run:

```bash
speakeasy quickstart
```

And follow the prompts.

## License

This project is licensed under the terms of the Apache 2.0 license.
