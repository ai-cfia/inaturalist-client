# coding: utf-8

# flake8: noqa

"""
iNaturalist API

# https://api.inaturalist.org/v1/  [iNaturalist](https://www.inaturalist.org/) is a global community of naturalists, scientists, and members of the public sharing over a million wildlife sightings to teach one another about the natural world while creating high quality citizen science data for science and conservation.  These API methods return data in JSON/JSONP and PNG response formats. They are meant to supplement the existing [iNaturalist API](https://www.inaturalist.org/pages/api+reference), implemented in Ruby on Rails, which has more functionality and supports more write operations, but tends to be slower and have less consistent response formats. Visit our [developers page](https://www.inaturalist.org/pages/developers) for more information. Write operations that expect and return JSON describe a single `body` parameter that represents the request body, which should be specified as JSON. See the \"Model\" of each body parameter for attributes that we accept in these JSON objects.  Multiple values for a single URL parameter should be separated by commas, e.g. `taxon_id=1,2,3`.  Map tiles are generated using the [node-mapnik](https://github.com/mapnik/node-mapnik) library, following the XYZ map tiling scheme. The \"Observation Tile\" methods accept nearly all the parameters of the observation search APIs, and will generate map tiles reflecting the same observations returned by searches. These \"Observation Tile\" methods have corresponding [UTFGrid](https://github.com/mapbox/utfgrid-spec) JSON responses which return information needed to make interactive maps.  Authentication in the Node API is handled via JSON Web Tokens (JWT). To obtain one, make an [OAuth-authenticated request](http://www.inaturalist.org/pages/api+reference#auth) to https://www.inaturalist.org/users/api_token. Each JWT will expire after 24 hours. Authentication required for all PUT and POST requests. Some GET requests will also include private information like hidden coordinates if the authenticated user has permission to view them.  Photos served from https://static.inaturalist.org and https://inaturalist-open-data.s3.amazonaws.com have multiple size variants and not all size variants are returned in responses. To access other sizes, the photo URL can be modified to replace only the size qualifier (each variant shares the exact same extension). The domain a photo is hosted under reflects the license under which the photo is being shared, and the domain may change over time if the license changes. Photos in the `inaturalist-open-data` domain are shared under open licenses. These can be accessed in bulk in the [iNaturalist AWS Open Dataset]( https://registry.opendata.aws/inaturalist-open-data/). Photos in the `static.inaturalist.org` domain do not have open licenses.  The available photo sizes are: * original (max 2048px in either dimension) * large (max 1024px in either dimension) * medium (max 500px in either dimension) * small (max 240px in either dimension) * thumb (max 100px in either dimension) * square (75px square)  iNaturalist Website: https://www.inaturalist.org/  Open Source Software: https://github.com/inaturalist/  ## Terms of Use  Use of this API is subject to the iNaturalist [Terms of Service](https://www.inaturalist.org/terms) and [Privacy Policy](https://www.inaturalist.org/privacy). We will block any use of our API that violates our Terms or Privacy Policy without notice. The API is intended to support application development, not data scraping. For pre- generated data exports, see https://www.inaturalist.org/pages/developers.  Please note that we throttle API usage to a max of 100 requests per minute, though we ask that you try to keep it to 60 requests per minute or lower, and to keep under 10,000 requests per day. If we notice usage that has serious impact on our performance we may institute blocks without notification.  Terms of Service: https://www.inaturalist.org/terms  Privacy Policy: https://www.inaturalist.org/privacy

The version of the OpenAPI document: 1.3.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

__version__ = "1.0.0"

# import apis into sdk package
from inaturalist_client.api.annotations_api import AnnotationsApi
from inaturalist_client.api.comments_api import CommentsApi
from inaturalist_client.api.controlled_terms_api import ControlledTermsApi
from inaturalist_client.api.flags_api import FlagsApi
from inaturalist_client.api.identifications_api import IdentificationsApi
from inaturalist_client.api.messages_api import MessagesApi
from inaturalist_client.api.observation_field_values_api import (
    ObservationFieldValuesApi,
)
from inaturalist_client.api.observation_photos_api import ObservationPhotosApi
from inaturalist_client.api.observation_tiles_api import ObservationTilesApi
from inaturalist_client.api.observations_api import ObservationsApi
from inaturalist_client.api.photos_api import PhotosApi
from inaturalist_client.api.places_api import PlacesApi
from inaturalist_client.api.polygon_tiles_api import PolygonTilesApi
from inaturalist_client.api.posts_api import PostsApi
from inaturalist_client.api.project_observations_api import ProjectObservationsApi
from inaturalist_client.api.projects_api import ProjectsApi
from inaturalist_client.api.search_api import SearchApi
from inaturalist_client.api.taxa_api import TaxaApi
from inaturalist_client.api.users_api import UsersApi
from inaturalist_client.api.utf_grid_api import UTFGridApi
from inaturalist_client.api_client import ApiClient

# import ApiClient
from inaturalist_client.api_response import ApiResponse
from inaturalist_client.configuration import Configuration
from inaturalist_client.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from inaturalist_client.models.autocomplete_taxon import AutocompleteTaxon
from inaturalist_client.models.base_response import BaseResponse
from inaturalist_client.models.color import Color
from inaturalist_client.models.comment import Comment
from inaturalist_client.models.conservation_status import ConservationStatus
from inaturalist_client.models.core_place import CorePlace
from inaturalist_client.models.core_taxon import CoreTaxon
from inaturalist_client.models.date_details import DateDetails
from inaturalist_client.models.error import Error
from inaturalist_client.models.establishment_means import EstablishmentMeans
from inaturalist_client.models.fave import Fave
from inaturalist_client.models.field_value import FieldValue
from inaturalist_client.models.identification import Identification
from inaturalist_client.models.identifications_response import IdentificationsResponse
from inaturalist_client.models.message import Message
from inaturalist_client.models.messages_id_get200_response import (
    MessagesIdGet200Response,
)
from inaturalist_client.models.messages_response import MessagesResponse
from inaturalist_client.models.messages_unread_get200_response import (
    MessagesUnreadGet200Response,
)
from inaturalist_client.models.nearby_places_response import NearbyPlacesResponse
from inaturalist_client.models.nearby_places_response_all_of_results import (
    NearbyPlacesResponseAllOfResults,
)
from inaturalist_client.models.non_owner_identification import NonOwnerIdentification
from inaturalist_client.models.observation import Observation
from inaturalist_client.models.observation_taxon import ObservationTaxon
from inaturalist_client.models.observations_observers_response import (
    ObservationsObserversResponse,
)
from inaturalist_client.models.observations_observers_response_all_of_results import (
    ObservationsObserversResponseAllOfResults,
)
from inaturalist_client.models.observations_response import ObservationsResponse
from inaturalist_client.models.observations_show_response import (
    ObservationsShowResponse,
)
from inaturalist_client.models.photo import Photo
from inaturalist_client.models.places_response import PlacesResponse
from inaturalist_client.models.point_geo_json import PointGeoJson
from inaturalist_client.models.polygon_geo_json import PolygonGeoJson
from inaturalist_client.models.post_annotation import PostAnnotation
from inaturalist_client.models.post_annotation_annotation import (
    PostAnnotationAnnotation,
)
from inaturalist_client.models.post_comment import PostComment
from inaturalist_client.models.post_comment_comment import PostCommentComment
from inaturalist_client.models.post_flag import PostFlag
from inaturalist_client.models.post_flag_flag import PostFlagFlag
from inaturalist_client.models.post_identification import PostIdentification
from inaturalist_client.models.post_identification_identification import (
    PostIdentificationIdentification,
)
from inaturalist_client.models.post_message import PostMessage
from inaturalist_client.models.post_message_message import PostMessageMessage
from inaturalist_client.models.post_observation import PostObservation
from inaturalist_client.models.post_observation_field_value import (
    PostObservationFieldValue,
)
from inaturalist_client.models.post_observation_field_value_observation_field_value import (
    PostObservationFieldValueObservationFieldValue,
)
from inaturalist_client.models.post_observation_observation import (
    PostObservationObservation,
)
from inaturalist_client.models.post_observation_photo import PostObservationPhoto
from inaturalist_client.models.post_observation_photo_observation_photo import (
    PostObservationPhotoObservationPhoto,
)
from inaturalist_client.models.post_observation_vote import PostObservationVote
from inaturalist_client.models.post_post import PostPost
from inaturalist_client.models.post_post_post import PostPostPost
from inaturalist_client.models.post_project_add import PostProjectAdd
from inaturalist_client.models.post_project_observation import PostProjectObservation
from inaturalist_client.models.post_quality import PostQuality
from inaturalist_client.models.post_user import PostUser
from inaturalist_client.models.post_user_update_session import PostUserUpdateSession
from inaturalist_client.models.post_user_user import PostUserUser
from inaturalist_client.models.post_vote import PostVote
from inaturalist_client.models.project import Project
from inaturalist_client.models.project_member import ProjectMember
from inaturalist_client.models.project_members_response import ProjectMembersResponse
from inaturalist_client.models.project_observation_rule import ProjectObservationRule
from inaturalist_client.models.projects_response import ProjectsResponse
from inaturalist_client.models.put_flag import PutFlag
from inaturalist_client.models.put_flag_flag import PutFlagFlag
from inaturalist_client.models.raw_conservation_status import RawConservationStatus
from inaturalist_client.models.show_observation import ShowObservation
from inaturalist_client.models.show_place import ShowPlace
from inaturalist_client.models.show_taxon import ShowTaxon
from inaturalist_client.models.sound import Sound
from inaturalist_client.models.species_counts_response import SpeciesCountsResponse
from inaturalist_client.models.species_counts_response_all_of_results import (
    SpeciesCountsResponseAllOfResults,
)
from inaturalist_client.models.taxa_autocomplete_response import (
    TaxaAutocompleteResponse,
)
from inaturalist_client.models.taxa_show_response import TaxaShowResponse
from inaturalist_client.models.taxon import Taxon
from inaturalist_client.models.taxon_conservation_status import TaxonConservationStatus
from inaturalist_client.models.taxon_photo import TaxonPhoto
from inaturalist_client.models.update_project_observation import (
    UpdateProjectObservation,
)
from inaturalist_client.models.update_project_observation_project_observation import (
    UpdateProjectObservationProjectObservation,
)
from inaturalist_client.models.user import User
from inaturalist_client.models.user_counts_response import UserCountsResponse
from inaturalist_client.models.user_counts_response_all_of_results import (
    UserCountsResponseAllOfResults,
)
from inaturalist_client.models.utf_grid_response import UTFGridResponse
