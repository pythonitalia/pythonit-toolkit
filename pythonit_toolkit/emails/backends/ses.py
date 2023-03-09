import json
from typing import Any, Dict, List, Optional
import html
import boto3
from pythonit_toolkit.emails.templates import EmailTemplate
from pythonit_toolkit.emails.utils import SafeString

from .base import EmailBackend


class SESEmailBackend(EmailBackend):
    def __init__(self, environment: str) -> None:
        super().__init__(environment)
        self.ses = boto3.client("ses")

    def send_email(
        self,
        *,
        template: EmailTemplate,
        subject: str,
        from_: str,
        to: str,
        variables: Optional[Dict[str, str]] = None,
        reply_to: List[str] = None,
    ):
        reply_to = reply_to or []

        variables = self.encode_vars({"subject": subject, **(variables or {})})
        self.ses.send_templated_email(
            Source=from_,
            Destination={"ToAddresses": [to]},
            Template=f"pythonit-{self.environment}-{template}",
            TemplateData=json.dumps(variables),
            ReplyToAddresses=reply_to,
            ConfigurationSetName='primary',
        )

    def encode_vars(self, variables: dict[str, Any]) -> dict[str, Any]:
        vars = dict()

        for key, value in variables.items():
            if isinstance(value, str) and not isinstance(value, SafeString):
                value = html.escape(value)

            vars[key] = value

        return vars
