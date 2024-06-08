from dataclasses import dataclass, asdict


@dataclass
class Record:
    date: str
    user_message: str
    user_key: int
    encrypted_message: str or None
    decrypted_message: str or None

    def to_save(self):
        return asdict(self)
