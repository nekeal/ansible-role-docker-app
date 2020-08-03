"""Role testing files using testinfra."""
import requests


def test_nginx_is_accessible(host):
    r = requests.get('http://localhost/')
    r.raise_for_status()
