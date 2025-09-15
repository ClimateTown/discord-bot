import pytest

import urllib

from spud.urls import UrlProcessor, YouTubeUrlProcessor, InstagramUrlProcessor

SOME_RANDOM_URL = (
    "https://some_random_website_not_matching_the_processors.com/path?foo=bar&v=123"
)


class ExampleUrlProcessor(UrlProcessor):
    """
    Takes in a URL. If domain is example.com, it changes it to xexample.com .

    Also removes all query parameters except for those with `?v=`.
    """

    def process(self, url: urllib.parse.ParseResult) -> urllib.parse.ParseResult:
        if url.netloc != "example.com":
            # if the domain is not example.com, we do nothing. We just return the url as is.
            return url

        url = url._replace(netloc="xexample.com")

        # Extract query params into a dictionary
        query_params = urllib.parse.parse_qs(url.query)

        # Keep only the 'v' parameter
        query_params = {k: v for k, v in query_params.items() if k == "v"}

        # Rebuild the query string and insert it back into the URL
        query = urllib.parse.urlencode(query_params, doseq=True)
        url = url._replace(query=query)

        return url


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param(
            urllib.parse.urlparse(SOME_RANDOM_URL),
            urllib.parse.urlparse(SOME_RANDOM_URL),
            id="no-op",
        ),
        pytest.param(
            urllib.parse.urlparse("https://example.com/path?foo=bar&v=123"),
            urllib.parse.urlparse("https://xexample.com/path?v=123"),
            id="strip-query-params-and-change-domain",
        ),
    ],
)
def test_example_url_processor(value, expected):
    processor = ExampleUrlProcessor()

    url = processor.process(value)

    assert url.geturl() == expected.geturl()


@pytest.mark.xfail(reason="Not implemented yet")
@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param(
            urllib.parse.urlparse(SOME_RANDOM_URL),
            urllib.parse.urlparse(SOME_RANDOM_URL),
            id="no-op",
        ),
        pytest.param(
            urllib.parse.urlparse(
                "https://example.com/path?foo=bar&v=123"
            ),  # TODO: EuroNuttella please update these, top one is value, bottom one is expected
            urllib.parse.urlparse("https://xexample.com/path?v=123"),
            id="strip-query-params-and-change-domain",
        ),
    ],
)
def test_youtube_url_processor(value, expected):
    processor = YouTubeUrlProcessor()

    url = processor.process(value)

    assert url.geturl() == expected.geturl()


@pytest.mark.xfail(reason="Not implemented yet")
@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param(
            urllib.parse.urlparse(SOME_RANDOM_URL),
            urllib.parse.urlparse(SOME_RANDOM_URL),
            id="no-op",
        ),
        pytest.param(
            urllib.parse.urlparse(
                "https://example.com/path?foo=bar&v=123"
            ),  # TODO: EuroNuttella please update these, top one is value, bottom one is expected
            urllib.parse.urlparse("https://xexample.com/path?v=123"),
            id="strip-query-params-and-change-domain",
        ),
    ],
)
def test_instagram_url_processor(value, expected):
    processor = InstagramUrlProcessor()

    url = processor.process(value)

    assert url.geturl() == expected.geturl()
