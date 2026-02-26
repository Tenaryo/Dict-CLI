#!/usr/bin/env python3
"""Dictionary CLI tool using Youdao API."""

import json
import sys
import urllib.request
import urllib.parse
import urllib.error


API_URL = "https://dict.youdao.com/jsonapi"


def fetch_word_data(word: str) -> dict:
    """Fetch word data from Youdao API."""
    params = {"q": word}
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"Network error: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Failed to parse API response", file=sys.stderr)
        sys.exit(1)


def extract_translations(data: dict) -> list[str]:
    """Extract word translations from API response."""
    translations = []
    
    # Primary translation from ec (English-Chinese)
    if "ec" in data:
        ec = data["ec"]
        if "word" in ec and len(ec["word"]) > 0:
            word_data = ec["word"][0]
            if "trs" in word_data:
                for tr_item in word_data["trs"]:
                    if "tr" in tr_item:
                        for tr in tr_item["tr"]:
                            if "l" in tr and "i" in tr["l"]:
                                meanings = tr["l"]["i"]
                                if isinstance(meanings, list):
                                    translations.extend(meanings)
                                elif isinstance(meanings, str):
                                    translations.append(meanings)
    
    return translations


def extract_examples(data: dict, count: int = 3) -> list[dict]:
    """Extract example sentences from API response."""
    examples = []
    
    # Bilingual sentences
    if "blng_sents_part" in data:
        sents = data["blng_sents_part"].get("sentence-pair", [])
        for sent in sents[:count]:
            if "sentence-eng" in sent:
                examples.append({
                    "en": sent["sentence-eng"].replace("<b>", "").replace("</b>", ""),
                    "zh": sent.get("sentence-translation", ""),
                    "source": sent.get("source", "")
                })
    
    return examples


def format_output(word: str, translations: list[str], examples: list[dict]) -> str:
    """Format the output for display."""
    lines = []
    
    # Translations
    if translations:
        lines.append(" ".join(translations))
    else:
        lines.append("未找到翻译")
    
    # Examples
    if examples:
        lines.append("")
        lines.append("例句:")
        for i, ex in enumerate(examples, 1):
            lines.append(f"{i}. {ex['en']}")
    
    return "\n".join(lines)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: dict <word>", file=sys.stderr)
        sys.exit(1)
    
    word = " ".join(sys.argv[1:])
    
    # Fetch data from API
    data = fetch_word_data(word)
    
    # Extract information
    translations = extract_translations(data)
    examples = extract_examples(data, count=3)
    
    # Output result
    print(format_output(word, translations, examples))


if __name__ == "__main__":
    main()
