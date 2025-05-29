# API for Automated Financial Analysis with Artificial Intelligence

```bash
VERSION = 1.0.0
```

Development of an API in Python for automated financial analysis using Artificial Intelligence. The application uses natural language models to identify possible signs of financial crisis in companies based on reading financial files, such as spreadsheets in XLSX format.

The project proposes an accessible and automated solution for micro, small and medium-sized companies to carry out preventive financial analysis. The tool aims to help identify early signs of crisis, such as:

- Falling turnover;
- Excessive indebtedness;
- Lack of liquidity;

Increased operating expenses.
By making financial analysis more democratic, the project contributes to bankruptcy prevention, promotes the financial health of small businesses and encourages data-based decision-making.

## prerequisites for running on your machine

- Have mysql installed on your machine
- Have a database created called **api_analise_financeira_automatizada**
- Create the following huggingface and cohere accounts [huggingface](https://huggingface.co/), [cohere](https://dashboard.cohere.com/welcome/login)
- Use the tokens created in huggingface and cohere by adding them to the variables **self.hugginface_token**, **self.cohere_token** inside  config.py

## Start the software

> git clone https://github.com/matheusmendes58/api_analise_financeira_automatizada.git

> cd api_analise_financeira_automatizada

> python -m venv venv

> cd venv/Scripts
 
> activate

> cd api_analise_financeira_automatizada

> pip install -r requirements.txt

> python main.py

## How to test the api

After starting main.py in your postman, use the following urls:

To bring in all the data entered the database use:

> GET - http://127.0.0.1:8000/analise/rpa/records/registry/

To retrieve the last data inserted into the database use:

> GET - http://127.0.0.1:8000/analise/rpa/records/registry/last

To analyze the file use:

Details - in body put form-data, key file and in value put the file to be analyzed, in the last part of the url (?service=cohere) put the service you want to use **cohere** or **huggingface**.

> POST - http://127.0.0.1:8000/analise/rpa/ai/send?service=cohere

To see the **sweeger** api documentation:

> GET - http://127.0.0.1:8000/documentation

> GET - http://127.0.0.1:8000/redoc-custom

## AI models used in the project

- Huggingface - There are a number of AI models to use. We're using one from google, but this model has a lot of errors in the api.

- Cohere - We use cohere chat, which is very efficient and free of charge. We recommend using this service on the endpoint.

## Business rule

Upload a xlsx file to the api endpoint, this api will process the file to send the data to an AI model to analyze if there are financial problems.

## Database tables

> registry_ia_error_or_success

| Column name         | Data Type     | Restrictions           | Description                                |
|------------------------|-------------------|-----------------------|--------------------------------------------|
| _id                    | INTEGER           | PRIMARY KEY, AUTOINCREMENT | Unique record identifier                   |
| execution              | DATETIME          |                       | Date and time of API execution             |
| file_name              | VARCHAR(250)      |                       | Name of the file analyzed                  |
| extension_file_name    | VARCHAR(100)      |                       | File extension                             |
| url_ia                 | TEXT              |                       | AI call URL                                |
| prompt_ia              | TEXT              |                       | Prompt sent to AI                          |
| status                 | VARCHAR(100)      |                       | General operation status (e.g. OK, Error)  |
| status_api             | VARCHAR(200)      |                       | API status code (e.g. 200 OK, 404)         |
| error_api              | TEXT              |                       | API error message (if any)                 |
| ai_error               | TEXT              |                       | Error returned by the AI                   |
| ai_text_success        | TEXT              |                       | Text returned by the AI in case of success |


## General notes

### This api is in version 1.0.0 and has a lot to be improved in terms of code and api response. Gradually, improvements will be made
