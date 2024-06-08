import json


class FileManager:
    def __init__(self):
        self.filename = "history.json"

    def save_to_file(self, memory: list):
        data_to_save = {}

        try:
            with open(self.filename, "r") as file:
                data_to_save = json.load(file)
        except FileNotFoundError:
            with open(self.filename, "x") as file:
                file.write("{}")

        records_in_file = len(data_to_save)

        for idx, record in enumerate(memory):
            data_to_save[idx + records_in_file] = record.to_save()

        with open(self.filename, "w") as file:
            json.dump(data_to_save, file, indent=4)

        print("Saved successfully!")

    def view_history(self, memory: list):
        try:
            with open(self.filename, "r") as file:
                data_to_read = json.load(file)

            for record in data_to_read.values():
                print(self.return_record_as_string(record))

        except FileNotFoundError:
            print("File not found")

        if memory:
            print("UNSAVED HISTORY")
            for record in memory:
                print(self.return_record_as_string(record.to_save()))

    @staticmethod
    def return_record_as_string(record: dict) -> str:
        record_as_string = (
            f"{record['date'][:19]}\n"
            f"Message: {record['user_message']}\n"
            f"Key: {record['user_key']}\n"
        )
        if record["encrypted_message"] is not None:
            record_as_string += f"Encrypted Message: {record['encrypted_message']}\n"
        else:
            record_as_string += f"Decrypted Message: {record['decrypted_message']}\n"
        return record_as_string
