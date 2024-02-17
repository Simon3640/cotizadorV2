from smtplib import SMTP_SSL
from email.mime.text import MIMEText

from app.core.logging import get_logger
from app.core.config import settings

log = get_logger(__name__)


class Email:
    def __init__(self, *, smtp_user: str, smtp_password: str) -> None:
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, *, subject: str, body: str, recipients: list[str]):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.smtp_user
        msg["To"] = ", ".join(recipients)
        with SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
            smtp_server.login(self.smtp_user, self.smtp_password)
            smtp_server.sendmail(self.smtp_user, recipients, msg.as_string())
            log.info("Mail sent successfully to " ", ".join(recipients))


email_svc = Email(smtp_password=settings.SMTP_PASSWORD, smtp_user=settings.SMTP_USER)
