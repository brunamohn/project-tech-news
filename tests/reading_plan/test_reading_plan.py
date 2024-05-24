import pytest
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501


def mocked_news():
    return [
        {"title": "Notícia 1", "reading_time": 4},
        {"title": "Notícia 2", "reading_time": 13},
        {"title": "Notícia 3", "reading_time": 20},
    ]


@pytest.fixture(autouse=True)
def mock(mocker):
    mocker.patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        mocked_news
    )


def test_reading_plan_group_news():
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)

    result = ReadingPlanService.group_news_for_available_time(4)

    assert result == {
        "readable": [
            {
                "unfilled_time": 0,
                "chosen_news": [
                    ("Notícia 1", 4),
                ],
            },
        ],
        "unreadable": [
            ("Notícia 2", 13),
            ("Notícia 3", 20),
        ],
    }
