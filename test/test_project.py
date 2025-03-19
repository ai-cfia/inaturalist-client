# coding: utf-8

"""
iNaturalist API

# https://api.inaturalist.org/v1/  [iNaturalist](https://www.inaturalist.org/) is a global community of naturalists, scientists, and members of the public sharing over a million wildlife sightings to teach one another about the natural world while creating high quality citizen science data for science and conservation.  These API methods return data in JSON/JSONP and PNG response formats. They are meant to supplement the existing [iNaturalist API](https://www.inaturalist.org/pages/api+reference), implemented in Ruby on Rails, which has more functionality and supports more write operations, but tends to be slower and have less consistent response formats. Visit our [developers page](https://www.inaturalist.org/pages/developers) for more information. Write operations that expect and return JSON describe a single `body` parameter that represents the request body, which should be specified as JSON. See the \"Model\" of each body parameter for attributes that we accept in these JSON objects.  Multiple values for a single URL parameter should be separated by commas, e.g. `taxon_id=1,2,3`.  Map tiles are generated using the [node-mapnik](https://github.com/mapnik/node-mapnik) library, following the XYZ map tiling scheme. The \"Observation Tile\" methods accept nearly all the parameters of the observation search APIs, and will generate map tiles reflecting the same observations returned by searches. These \"Observation Tile\" methods have corresponding [UTFGrid](https://github.com/mapbox/utfgrid-spec) JSON responses which return information needed to make interactive maps.  Authentication in the Node API is handled via JSON Web Tokens (JWT). To obtain one, make an [OAuth-authenticated request](http://www.inaturalist.org/pages/api+reference#auth) to https://www.inaturalist.org/users/api_token. Each JWT will expire after 24 hours. Authentication required for all PUT and POST requests. Some GET requests will also include private information like hidden coordinates if the authenticated user has permission to view them.  Photos served from https://static.inaturalist.org and https://inaturalist-open-data.s3.amazonaws.com have multiple size variants and not all size variants are returned in responses. To access other sizes, the photo URL can be modified to replace only the size qualifier (each variant shares the exact same extension). The domain a photo is hosted under reflects the license under which the photo is being shared, and the domain may change over time if the license changes. Photos in the `inaturalist-open-data` domain are shared under open licenses. These can be accessed in bulk in the [iNaturalist AWS Open Dataset]( https://registry.opendata.aws/inaturalist-open-data/). Photos in the `static.inaturalist.org` domain do not have open licenses.  The available photo sizes are: * original (max 2048px in either dimension) * large (max 1024px in either dimension) * medium (max 500px in either dimension) * small (max 240px in either dimension) * thumb (max 100px in either dimension) * square (75px square)  iNaturalist Website: https://www.inaturalist.org/  Open Source Software: https://github.com/inaturalist/  ## Terms of Use  Use of this API is subject to the iNaturalist [Terms of Service](https://www.inaturalist.org/terms) and [Privacy Policy](https://www.inaturalist.org/privacy). We will block any use of our API that violates our Terms or Privacy Policy without notice. The API is intended to support application development, not data scraping. For pre- generated data exports, see https://www.inaturalist.org/pages/developers.  Please note that we throttle API usage to a max of 100 requests per minute, though we ask that you try to keep it to 60 requests per minute or lower, and to keep under 10,000 requests per day. If we notice usage that has serious impact on our performance we may institute blocks without notification.  Terms of Service: https://www.inaturalist.org/terms  Privacy Policy: https://www.inaturalist.org/privacy

The version of the OpenAPI document: 1.3.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from inaturalist_client.models.project import Project


@unittest.skip("Skipping all tests in TestProject")
class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Project:
        """Test Project
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Project`
        """
        model = Project()
        if include_optional:
            return Project(
                id = 56,
                title = '',
                description = '',
                slug = ''
            )
        else:
            return Project(
        )
        """

    def testProject(self):
        """Test Project"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
