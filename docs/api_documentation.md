# Drug Information API Documentation
## Overview
## The Drug Information API provides access to a database of pharmaceutical data, including drugs, targets, diseases, and drug-target interactions. This documentation outlines the endpoints, request parameters, response formats, and usage examples for interacting with the API.

### Authentication
The API uses API keys for authentication. Include your API key in the Authorization header of each request.


makefile
Copy code
Authorization: Bearer YOUR_API_KEY
Endpoints
1. Get Drug Information
Endpoint
URL: /drugs/{id}
Method: GET
Description: Retrieve information about a specific drug by its ID.
Request Parameters
id (required): ID of the drug to retrieve information for.
Response
Status Code: 200 OK
Body:
json
Copy code
{
  "id": "D00107",
  "name": "Lisinopril",
  "description": "Lisinopril is a medication used to treat high blood pressure..."
  "targets": [
    {
      "id": "P00734",
      "name": "Angiotensin-converting enzyme"
    },
    {
      "id": "P35225",
      "name": "Endothelin receptor type B"
    }
  ],
  "indications": [
    "Hypertension",
    "Heart failure"
  ]
}
Example
Request:

bash
Copy code
GET /api/v1/drugs/D00107
Authorization: Bearer YOUR_API_KEY
Response:

json
Copy code
{
  "id": "D00107",
  "name": "Lisinopril",
  "description": "Lisinopril is a medication used to treat high blood pressure...",
  "targets": [
    {
      "id": "P00734",
      "name": "Angiotensin-converting enzyme"
    },
    {
      "id": "P35225",
      "name": "Endothelin receptor type B"
    }
  ],
  "indications": [
    "Hypertension",
    "Heart failure"
  ]
}
2. Search Drugs
Endpoint
URL: /drugs/search
Method: GET
Description: Search for drugs based on name or keyword.
Request Parameters
query (required): Search query for drug names or keywords.
Response
Status Code: 200 OK
Body:
json
Copy code
[
  {
    "id": "D00368",
    "name": "Lipitor",
    "description": "Lipitor is a statin medication used to lower cholesterol levels..."
  },
  {
    "id": "D00109",
    "name": "Aspirin",
    "description": "Aspirin is a nonsteroidal anti-inflammatory drug used to reduce pain..."
  }
]
Example
Request:

sql
Copy code
GET /api/v1/drugs/search?query=Lipitor
Authorization: Bearer YOUR_API_KEY
Response:

json
Copy code
[
  {
    "id": "D00368",
    "name": "Lipitor",
    "description": "Lipitor is a statin medication used to lower cholesterol levels..."
  }
]
Rate Limiting
The API has rate limiting in place to prevent abuse. The rate limit is set at 100 requests per hour per API key.

Error Responses
400 Bad Request: Invalid request parameters or format.
401 Unauthorized: Missing or invalid API key.
404 Not Found: Resource not found.
429 Too Many Requests: Rate limit exceeded.

