def reverse_string(value: str) -> str:
    return value[::-1]

class FilterModule:
    def filters(self) -> dict:
        return {
            "reverse_string": reverse_string
        }
