import pytest
from flask import Flask

# Test the route with an invalid request method
def test_home_route_invalid_method():
    # Use Flask's test client to simulate requests
    with app.test_client() as client:
        response = client.post('/')  # Send POST request instead of GET
        assert response.status_code == 405  # Expecting "Method Not Allowed"
