from __future__ import annotations

import path_planning as pp


def test_version():
    assert pp.__version__ == "0.0.1"


def test_generate():
    assert pp.generate(5, 2) == 5000


def test_describe():
    assert pp.describe(1, 2) == 1000
