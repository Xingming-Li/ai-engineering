from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int
    
    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value
    
user = User(
    name = "Jack",
    email = "jack@gmail.com",
    account_id = 1234
)

print("Old user:")
print(user.name)
print(user.email)
print(user.account_id)

# user_json_str = user.model_dump_json()

new_user_json_str = '{"name": "Mike", "email": "mike@gmail.com", "account_id": 234}'
new_user = User.model_validate_json(new_user_json_str)

print("\nNew user:")
print(new_user.name)
print(new_user.email)
print(new_user.account_id)