from contextlib import nullcontext as does_not_raise
from copy import deepcopy

from sqlalchemy_utils import Ltree

from src.schemas.user import UserSchema
from tests.fakes import FAKE_USERS

# kwargs, expected_result, expectation
TEST_BASE_SERVICE_GET_BY_QUERY_ONE_OR_NONE_PARAMS = [
    ({"id": 2}, FAKE_USERS[1], does_not_raise()),
    ({"id": 4}, None, does_not_raise()),
]

# kwargs, expected_result, expectation
TEST_BASE_SERVICE_GET_BY_QUERY_ALL_PARAMS = [
    ({"id": 2}, [FAKE_USERS[1]], does_not_raise()),
    ({"id": 4}, None, does_not_raise()),
]

# kwargs, expected_result, expectation
TEST_BASE_SERVICE_UPDATE_ONE_BY_ID_PARAMS = [
    (
        {"_id": FAKE_USERS[0].id, "uuid": "a-a-A"},
        UserSchema(
            id=FAKE_USERS[0].id,
            uuid="a-a-A",
            path=Ltree('1')
        ),
        does_not_raise(),
    ),
]

# kwargs, expected_result, expectation
TEST_BASE_SERVICE_DELETE_BY_QUERY_PARAMS = [
    ({"id": FAKE_USERS[0].id}, FAKE_USERS[1:], does_not_raise()),
]

# kwargs, expected_result, expectation
TEST_SQLALCHEMY_REPOSITORY_GET_BY_QUERY_ONE_OR_NONE_PARAMS = deepcopy(
    TEST_BASE_SERVICE_GET_BY_QUERY_ONE_OR_NONE_PARAMS
)

# kwargs, expected_result, expectation
TEST_SQLALCHEMY_REPOSITORY_GET_BY_QUERY_ALL_PARAMS = deepcopy(
    TEST_BASE_SERVICE_GET_BY_QUERY_ALL_PARAMS
)

# kwargs, expected_result, expectation
TEST_SQLALCHEMY_REPOSITORY_UPDATE_ONE_BY_ID_PARAMS = deepcopy(
    TEST_BASE_SERVICE_UPDATE_ONE_BY_ID_PARAMS
)


# kwargs, expected_result, expectation
TEST_SQLALCHEMY_REPOSITORY_DELETE_BY_QUERY_PARAMS = deepcopy(
    TEST_BASE_SERVICE_DELETE_BY_QUERY_PARAMS
)
