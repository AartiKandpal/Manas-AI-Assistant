import json
import re

from core.logger import logger


def parse_json(text: str) -> dict:
    """
    Extracts and parses the first JSON object returned by the LLM.

    Always returns a dictionary in the format:

    {
        "tools": [],
        "response": "..."
    }
    """

    text = text.strip()

    # -------------------------------------------------
    # Case 1: Pure JSON
    # -------------------------------------------------

    try:
        data = json.loads(text)

        if isinstance(data, dict):
            data.setdefault("tools", [])
            data.setdefault("response", "")
            return data

    except Exception:
        pass

    # -------------------------------------------------
    # Case 2: JSON inside markdown
    # -------------------------------------------------

    markdown = re.search(
        r"```(?:json)?\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )

    if markdown:

        try:
            data = json.loads(markdown.group(1))

            data.setdefault("tools", [])
            data.setdefault("response", "")

            return data

        except Exception:
            pass

    # -------------------------------------------------
    # Case 3: First JSON object
    # -------------------------------------------------

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL,
    )

    if match:

        candidate = match.group(0)

        # Auto-close missing braces
        diff = candidate.count("{") - candidate.count("}")

        if diff > 0:
            candidate += "}" * diff

        try:

            data = json.loads(candidate)

            data.setdefault("tools", [])
            data.setdefault("response", "")

            return data

        except Exception:

            logger.exception(
                "Failed parsing extracted JSON."
            )

    # -------------------------------------------------
    # Case 4: Plain text fallback
    # -------------------------------------------------

    logger.error(
        "Invalid model output:\n%s",
        text,
    )

    return {
        "tools": [],
        "response": text,
    }