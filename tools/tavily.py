
from tavily import TavilyClient
from dotenv import load_dotenv
import os
import time
import requests

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError(
        "TAVILY_API_KEY is missing. Check your .env file."
    )

client = TavilyClient(api_key=api_key)


def tavily_search(query: str) -> str:
    """Search Tavily and format results with retry handling."""

    for attempt in range(3):
        try:
            response = client.search(
                query=query,
                max_results=5,
                timeout=30,
            )

            results = response.get("results", [])
            formatted_results = []

            for i, item in enumerate(results, 1):
                title = item.get("title", "Unknown")
                url = item.get("url", "")
                snippet = item.get("content", "").strip()

                if len(snippet) > 300:
                    snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

                formatted_results.append(
                    f"{i}. **{title}**\n"
                    f"URL: {url}\n"
                    f"{snippet}"
                )

            if not formatted_results:
                return "No search results were found."

            return "\n\n".join(formatted_results)

        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
        ) as exc:
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
            else:
                return (
                    "Hotel search is temporarily unavailable due to "
                    f"a connection issue ({type(exc).__name__}). "
                    "Please try again."
                )

        except Exception as exc:
            return f"Tavily search failed: {type(exc).__name__}: {exc}"

    return "Hotel search is temporarily unavailable."
