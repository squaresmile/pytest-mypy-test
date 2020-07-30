import pytest

@pytest.mark.parametrize("query,result", [("q", "r")])
def test_raw(query: str, result: str) -> None:
    pass

reveal_type(test_raw)
