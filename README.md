# iNaturalist Python Client

## Requirements

Python 3.8+

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```

(you may need to run `pip` with root permission: `sudo pip install
git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:

```python
import inaturalist_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import inaturalist_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run
the following:

```python

import inaturalist_client
from inaturalist_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = inaturalist_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'


# Enter a context with an instance of the API client
async with inaturalist_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = inaturalist_client.AnnotationsApi(api_client)
    id = 'id_example' # str | ID or UUID of the annotation

    try:
        # Annotation Delete
        await api_instance.annotations_id_delete(id)
    except ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_id_delete: %s\n" % e)

```
