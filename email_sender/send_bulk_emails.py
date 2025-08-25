import send_single_email

#function create bulk email send 
def send_bulk_emails(emails:list, subject:str, body:str):
    for to_email in emails:
        try:
            send_single_email.single_sender(
                to_email= to_email,
                subject=subject,
                body=body
            )
            print(f"Email send successfully to {to_email}")
        except Exception as e:
            print(f"Failed to send email to {to_email}.Error : {e}")