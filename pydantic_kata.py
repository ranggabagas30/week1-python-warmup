"""Small Pydantic example for validating invoice data.

Pydantic lets us define the expected shape of data with normal Python type
hints, then validate raw input before the rest of the program uses it.
"""

from pydantic import BaseModel, Field


class Invoice(BaseModel):
    """Validated invoice data model.

    Each class attribute is a field on the model. Pydantic uses the type hints
    to parse and validate incoming data.
    """

    vendor: str
    total: float = Field(gt=0)  # Require total to be greater than 0.
    currency: str = "SGD"  # Use SGD when the input does not provide currency.
    line_items: list[str] = []  # Optional list of item names on the invoice.


# Raw JSON often comes from an API, file, queue, or LLM response.
raw = '{"vendor": "Acme", "total": 128.5}'

# Validate the JSON string and convert it into an Invoice object.
# This raises a ValidationError if required fields are missing or invalid.
inv = Invoice.model_validate_json(raw)

# Access validated fields with normal dot notation.
print(inv.total)  # 128.5, as a float
