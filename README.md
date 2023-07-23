# PYSTART v2 API

The ***pystart-v2-api*** is a RESTful API that provides information about the earnings of junior Python developers. The API has a single endpoint, ```/```, which returns the earnings of juniors for the specified number of days.

## Paramaters

The endpoint takes a query parameter, ```days```, which specifies the number of days to get the earnings for. The default value for ```days``` is **10**.

## Responses

The response from the endpoint is a dictionary with the following keys:

    date_last_update: The date the result file was last updated.
    python: The earnings of juniors for the specified number of days.

## Raises

If ```days``` is not a positive integer, the API will raise a **ValueError** exception.

## Example request

Here is an example of a request to the endpoint:

```GET /?days=20```

The response to this request would be a dictionary with the following keys:

date_last_update: The date the result file was last updated.
python: The earnings of juniors for the past 20 days.

---

*Docstrings and readme are prepared with the help of Google Bard*