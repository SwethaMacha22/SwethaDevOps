import pytest
from flask import Flask


def test_home_route_invalid_method():
    
    with app.test_client() as client:
        response = client.post('/')  # Send POST request instead of GET
        assert response.status_code == 405  # Expecting "Method Not Allowed"
