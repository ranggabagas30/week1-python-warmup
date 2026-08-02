# Import the Pydantic tools used in this example.
# - BaseModel: the parent class for creating validated data models.
# - Field: lets us add extra validation rules and metadata to one field.
# - ValidationError: the error type Pydantic raises when data fails validation.
from pydantic import BaseModel, Field, ValidationError


# A Pydantic model is a Python class that describes the expected shape of data.
# TraineeProfile represents one trainee's profile and the type each value should have.
# Because it inherits from BaseModel, Pydantic automatically checks incoming data.
class TraineeProfile(BaseModel):
    # name is required because it has no default value.
    # The ': str' type hint means Pydantic expects this value to be a string.
    name: str

    # years_experience is also required.
    # Field(...) means: this field is required, but we want extra validation rules.
    # The three dots '...' are Python's Ellipsis object; Pydantic uses it here to
    # say "no default value is provided, so the caller must provide this field."
    # ge=0 means "greater than or equal to 0". This prevents negative experience.
    # description is human-readable metadata. It can appear in generated schemas
    # or documentation, but it is not the validation rule itself.
    years_experience: int = Field(
        ...,
        ge=0,
        description="Years of experience must be a non-negative integer.",
    )

    # current_role is required and must be a string, for example "BA" or "Developer".
    current_role: str

    # target_role is optional because it has a default value.
    # If the input data does not include target_role, Pydantic uses "AI Engineer".
    target_role: str = "AI Engineer"

    # skills is optional because it has a default empty list.
    # The type hint list[str] means this should be a list where every item is a string.
    skills: list[str] = []


# good is a JSON string that contains valid trainee data.
# It includes all required fields: name, years_experience, and current_role.
# It does not include target_role or skills, so Pydantic will use their defaults.
good = '{"name": "Ana", "years_experience": 7, "current_role": "BA"}'

# model_validate_json reads the JSON string, validates the values, and returns
# a TraineeProfile object if everything is valid.
print(TraineeProfile.model_validate_json(good))

# bad is another JSON string, but this one is invalid.
# years_experience is -1, which breaks the Field rule ge=0.
bad = '{"name": "Ana", "years_experience": -1, "current_role": "BA"}'

# The try block attempts to validate the bad JSON.
# Since years_experience is negative, Pydantic raises a ValidationError.
try:
    print(TraineeProfile.model_validate_json(bad))

# The except block catches that ValidationError and stores it in variable e.
# Printing e shows which field failed, what rule failed, and what input caused it.
except ValidationError as e:
    print("Validation error:", e)

class Patient(BaseModel):
    name: str
    age: int = Field(..., ge=0, description="Age must be a non-negative integer.")
    medical_history: list[str] = []

class Nurse(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Name of the nurse.")
    patients: list[Patient] = Field(..., description="List of patients assigned to the nurse.")
    start_date: str = Field(..., format="date", description="Start date of the nurse in YYYY-MM-DD format.")

john_doe_patient = {
    "name": "John Doe",
    "age": 30,
    "medical_history": ["Diabetes", "Hypertension"]
}   

nurse_data = {
    "name": "Alice Smith",
    "patients": [john_doe_patient],
    "start_date": "2023-01-01"
}

print(Patient.model_validate(john_doe_patient))
print (Nurse.model_validate(nurse_data))
print("Nurse's name:" + nurse_data["name"] + " is handling his patients: " + str(nurse_data["patients"]) + " since " + nurse_data["start_date"])