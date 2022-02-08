# Sky Backend API

**Crypto Currency Market API's**

* Used to get the last 24 hour market summary

Framework:
* Flask 1.1.4
* OpenAPI 3 (OAS3)
* Swagger UI

Security
* Bearer Authentication (HTTP bearer)

Testing
* Pytest

  running cmd: `pytest app\test_cases -v`

Application Run:

* Docker Build

    `NAME=sky_dev_api PORT=7005 docker-compose build -d`
* Docker Up

    `NAME=sky_dev_api PORT=7005 docker-compose up -d`

API's:

    prefix: api/v1/

    api endpoint:
       * /login - check login and generate auth token
       * /marketsummaries - get the last 24hr summary of all active markets
       * /marketsummary - get the last 24hr summary of specific market

