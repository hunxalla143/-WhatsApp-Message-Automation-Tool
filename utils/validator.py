import re


def normalize_phone(phone):
    """
    Convert phone to WhatsApp format.
    """

    phone = str(phone).strip()

    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")

    if not phone.startswith("+"):
        phone = "+" + phone

    return phone


def validate_phone(phone):
    phone = normalize_phone(phone)

    pattern = r"^\+\d{10,15}$"

    return bool(re.match(pattern, phone))