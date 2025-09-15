import abc

import urllib.parse


class UrlProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, url: urllib.parse.ParseResult) -> urllib.parse.ParseResult:
        """
        Takes in a URL, checks whether it needs to be sanitized, and returns a processed version of it.

        If no processing is needed, returns the original URL. See ExampleUrlProcessor in the `test_urls.py` file for an example implementation.
        """
        pass


class YouTubeUrlProcessor(UrlProcessor):
    ...


class InstagramUrlProcessor(UrlProcessor):
    ...


URL_PROCESSORS: list[UrlProcessor] = [
    # YouTubeUrlProcessor(),
    # InstagramUrlProcessor(),
]


def process_url(url: urllib.parse.ParseResult) -> urllib.parse.ParseResult:
    """Runs the URL through all registered processors, sequentially."""
    for processor in URL_PROCESSORS:
        url = processor.process(url)

    return url
