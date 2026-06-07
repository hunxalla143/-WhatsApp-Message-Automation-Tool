from services.whatsapp_service import (
    WhatsAppService
)

from services.template_manager import (
    TemplateManager
)

from utils.validator import (
    normalize_phone
)


class BulkSender:

    def __init__(self):

        self.sender = WhatsAppService()
        self.template_manager = TemplateManager()

    def send_bulk(
        self,
        contacts,
        template_name
    ):

        template = self.template_manager.get_template(
            template_name
        )

        if not template:
            print("Template not found.")
            return

        total = len(contacts)

        print(f"\nTotal Contacts: {total}")

        success = 0
        failed = 0

        for person in contacts:

            try:

                phone = normalize_phone(
                    person.get("phone", "")
                )

                message = (
                    self.template_manager.personalize(
                        template,
                        person
                    )
                )

                print(
                    f"\nSending to {person.get('name')}"
                )

                self.sender.send_message(
                    phone,
                    message
                )

                print("✓ Sent")

                success += 1

            except Exception as e:

                print(
                    f"✗ Failed: {e}"
                )

                failed += 1

        print("\n========== REPORT ==========")
        print(f"Success : {success}")
        print(f"Failed  : {failed}")
        print("============================")