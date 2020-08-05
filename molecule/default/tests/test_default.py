"""Role testing files using testinfra."""
import requests


def test_nginx_is_accessible(host):
    r = requests.get('http://localhost/')
    r.raise_for_status()


def test_file_is_created_during_pre_release_command(host):
    file = host.file("/tmp/pre_release_part")
    assert file.exists


def test_file_is_created_during_post_release_command(host):
    file = host.file('/tmp/post_release_part')
    assert file.exists


def test_post_release_is_executed_after_pre_release_command(host):
    pre_release_file = host.file("/tmp/pre_release_part")
    post_release_file = host.file("/tmp/post_release_part")
    assert pre_release_file.mtime < post_release_file.mtime
