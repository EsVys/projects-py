from sre_constants import SUCCESS
from unicodedata import name
import pytest
import bouncer

name = 'John'

def test_fail_bouncer_age_validation():
    with pytest.raises(SystemExit):
        bouncer.age_validation(6, name)

def test_success_bouncer_age_validation():
    bouncer.age_validation(16, name)

def test_success_bouncer_validate_input_age(monkeypatch):
    input = 20
    monkeypatch.setattr('builtins.input', lambda _: input)
    age = bouncer.validate_input_age(name)
    assert age == input

def test_success_evil_status_no(monkeypatch):
    input = 'no'
    name = 'Ben'
    monkeypatch.setattr('builtins.input', lambda _: input)
    bouncer.evil_status(name)