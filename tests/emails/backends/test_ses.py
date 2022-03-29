from unittest.mock import patch

from pythonit_toolkit.emails.backends.ses import SESEmailBackend
from pythonit_toolkit.emails.templates import EmailTemplate
from ward import test


@test("send email via ses")
async def _():
    with patch("pythonit_toolkit.emails.backends.ses.boto3") as mock_boto:
        SESEmailBackend("production").send_email(
            template=EmailTemplate.RESET_PASSWORD,
            subject="Subject",
            from_="test@email.it",
            to="destination@email.it",
            variables={"a": "b", "c": "d"},
        )

    mock_boto.client.return_value.send_templated_email.assert_called_once_with(
        Source="test@email.it",
        Destination={"ToAddresses": ["destination@email.it"]},
        Template="pythonit-production-reset-password",
        TemplateData='{"subject": "Subject", "a": "b", "c": "d"}',
        ReplyToAddresses=[],
        ConfigurationSetName='primary',
    )


@test("send email without variables")
async def _():
    with patch("pythonit_toolkit.emails.backends.ses.boto3") as mock_boto:
        SESEmailBackend("production").send_email(
            template=EmailTemplate.RESET_PASSWORD,
            subject="Subject",
            from_="test@email.it",
            to="destination@email.it",
        )

    mock_boto.client.return_value.send_templated_email.assert_called_once_with(
        Source="test@email.it",
        Destination={"ToAddresses": ["destination@email.it"]},
        Template="pythonit-production-reset-password",
        TemplateData='{"subject": "Subject"}',
        ReplyToAddresses=[],
        ConfigurationSetName='primary',
    )


@test("send email with reply to")
async def _():
    with patch("pythonit_toolkit.emails.backends.ses.boto3") as mock_boto:
        SESEmailBackend("production").send_email(
            template=EmailTemplate.RESET_PASSWORD,
            subject="Subject",
            from_="test@email.it",
            to="destination@email.it",
            reply_to=[
                "test1@placeholder.com",
                "test2@placeholder.com",
            ]
        )

    mock_boto.client.return_value.send_templated_email.assert_called_once_with(
        Source="test@email.it",
        Destination={"ToAddresses": ["destination@email.it"]},
        Template="pythonit-production-reset-password",
        TemplateData='{"subject": "Subject"}',
        ReplyToAddresses=[
            "test1@placeholder.com",
            "test2@placeholder.com",
        ],
        ConfigurationSetName='primary',
    )


@test("variables are html encoded")
async def _():
    with patch("pythonit_toolkit.emails.backends.ses.boto3") as mock_boto:
        SESEmailBackend("production").send_email(
            template=EmailTemplate.RESET_PASSWORD,
            subject="Subject",
            from_="test@email.it",
            to="destination@email.it",
            variables={
                "a": '<a href="https://google.it">link</a>',
            },
        )

    mock_boto.client.return_value.send_templated_email.assert_called_once_with(
        Source="test@email.it",
        Destination={"ToAddresses": ["destination@email.it"]},
        Template="pythonit-production-reset-password",
        TemplateData='{"subject": "Subject", "a": "&lt;a href=&quot;https://google.it&quot;&gt;link&lt;/a&gt;"}',
        ReplyToAddresses=[],
        ConfigurationSetName='primary',
    )
