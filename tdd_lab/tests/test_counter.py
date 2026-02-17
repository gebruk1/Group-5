"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
# ===========================
# Test: GET missing counter returns 404
# Author: Kaleab Gebru
# Date: 2026-02-14
# Description: Ensure GET returns JSON 404 when counter does not exist.
# ===========================

import pytest
from src import app
from src import status

@pytest.fixture()
def client():
    """Fixture for Flask test client"""
    return app.test_client()

@pytest.mark.usefixtures("client")
class TestCounterEndpoints:
    """Test cases for Counter API"""


    def test_get_missing_counter_returns_404(self, client):
        """It should return 404 for a counter that does not exist"""
        result = client.get("/counters/doesnotexist")
        assert result.status_code == status.HTTP_404_NOT_FOUND

        data = result.get_json()
        assert data is not None  # flask 404 is HTML get_json() 
        assert "error" in data
