"""Role testing files using testinfra."""
import requests


def test_nginx_is_accessible(host):
    r = requests.get('http://localhost/')
    r.raise_for_status()


def test_file_is_created_during_pre_release_command(host):
    file = host.file("/tmp/pre_release_part")
    assert file.exists
