import pytest

from charsleft_widget.widgets import CharsLeftArea


@pytest.mark.parametrize(
    ("value", "maxlength", "expected_current"),
    [
        pytest.param("test", 512, 508, id="within-limit"),
        pytest.param("x" * 20, 10, -10, id="over-limit"),
    ],
)
def test_render_shows_chars_left(
    value: str,
    maxlength: int,
    expected_current: int,
) -> None:
    widget = CharsLeftArea()

    html = widget.render("value", value, {"id": "id_field", "maxlength": maxlength})

    assert 'class="charsleft"' in html
    assert f'<span class="current">{expected_current}</span>' in html


def test_render_without_maxlength_falls_back_to_textarea() -> None:
    widget = CharsLeftArea()

    html = widget.render("value", None, {"id": "id_field"})

    assert html.startswith("<textarea")
    assert "charsleft" not in html
