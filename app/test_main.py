import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

@pytest.mark.parametrize('json_data, status, results',
                             [({
                                "displaystring_holder": "question.tire1_r_profile_picture",
                                "locale": "en-GB",
                                "context": "offer"
                                }, 200, 'Photo of tire profile of 1st axle | Passenger side'),
                              ({}, 422, 'Unprocessable Entity'),])
def test_get_display_strings(json_data, status, results):
    response = client.post(
        "/context_display_strings/",
        json=json_data,
    )
    assert response.status_code == status
    if status != 422:
        assert response.json() == results
    
@pytest.mark.parametrize('json_data, status, results',
                             [({
                                "dictionary": {
                                    "displayStringUID": "question.tire1_r_profile",
                                        "subdocument_01": [{
                                        "displayStringUID": "question.tire1_r_profile"}]
                                        },
                                "locale": "en-GB",
                                "context": "offer"
                                }, 200, {
                                        "displayStringUID": "Tire profile at 1st axle | Passenger side",
                                            "subdocument_01": [
                                                {
                                                    "displayStringUID": "Tire profile at 1st axle | Passenger side"
                                                }
                                            ]
                                        }),
                              ({}, 422, 'Unprocessable Entity'),])    
def test_resolve_display_strings(json_data, status, results):
    response = client.post(
        "/resolve_display_strings/",
        json=json_data,
    )
    assert response.status_code == status
    if status != 422:
        assert response.json() == results

    