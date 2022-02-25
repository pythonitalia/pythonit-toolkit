from enum import Enum


class EmailTemplate(str, Enum):
    RESET_PASSWORD = "reset-password"
    NEW_COMMENT_ON_SUBMISSION = "new-comment-on-submission"
    SUBMISSION_ACCEPTED = "submission-accepted"

    def __str__(self) -> str:
        return str.__str__(self)
