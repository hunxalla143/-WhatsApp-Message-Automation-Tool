from colorama import init, Fore

from services.whatsapp_service import (
    WhatsAppService
)

from services.bulk_sender import (
    BulkSender
)

from services.template_manager import (
    TemplateManager
)

from scheduler.scheduler import (
    MessageScheduler
)

from utils.file_handler import (
    load_csv,
    load_json
)

init()

sender = WhatsAppService()
bulk = BulkSender()
scheduler = MessageScheduler()

def menu():

    while True:

        print(Fore.CYAN + "\n" + "="*50)
        print("WHATSAPP AUTOMATION TOOL")
        print("="*50)

        print("1. Send Message")
        print("2. Bulk Messaging")
        print("3. Use Template")
        print("4. Schedule Message")
        print("5. View Logs")
        print("6. Exit")

        choice = input("\nChoice: ")

        if choice == "1":

            phone = input("Phone: ")
            msg = input("Message: ")

            try:
                sender.send_message(
                    phone,
                    msg
                )

                print("Message Sent")

            except Exception as e:
                print(e)

        elif choice == "2":

            file_type = input(
                "CSV or JSON? "
            ).lower()

            if file_type == "csv":
                contacts = load_csv(
                    "contacts/contacts.csv"
                )
            else:
                contacts = load_json(
                    "contacts/contacts.json"
                )

            bulk.send_bulk(
                contacts,
                "marketing"
            )

        elif choice == "3":

            manager = TemplateManager()

            template = manager.get_template(
                "course_reminder"
            )

            data = {
                "name": input("Name: "),
                "course": input("Course: ")
            }

            message = manager.personalize(
                template,
                data
            )

            print("\nPreview:")
            print(message)

        elif choice == "4":

            phone = input("Phone: ")
            msg = input("Message: ")
            schedule_time = input(
                "Time (HH:MM): "
            )

            scheduler.schedule_message(
                lambda:
                sender.send_message(
                    phone,
                    msg
                ),
                schedule_time
            )

        elif choice == "5":

            try:

                with open(
                    "logs/messages.log",
                    "r"
                ) as file:

                    print(file.read())

            except:
                print("No Logs Found")

        elif choice == "6":
            break

        else:
            print("Invalid Option")

menu()
