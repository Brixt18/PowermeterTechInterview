import datetime


def get_text_or_empty(text: str, strip=False) -> str:
    if (not text) or (text.isspace()):
        return ""

    return text.strip() if strip else text


def get_text_or_none(text: str, strip=False) -> str:
    if (not text) or (text.isspace()):
        return None

    return text.strip() if strip else text


def strip_dict_fields(data: dict) -> dict:
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = value.strip()

    return data


def strip_list_fields(data: list) -> list:
    _data = []

    for item in data:
        if isinstance(item, str):
            _data.append(item.strip())

        else:
            _data.append(item)

    return _data


def delete_duplicate_from_list(data: list) -> list:
    _data = []
    for item in data:
        if item not in _data:
            _data.append(item)

    return _data


def parse_datetime_to_iso8601(date: datetime) -> str:
    return date.isoformat()
