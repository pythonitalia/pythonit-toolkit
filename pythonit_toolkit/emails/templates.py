from enum import Enum


class EmailTemplate(str, Enum):
    # Grants
    GRANT_APPROVED_TICKET_ONLY = "grant-approved-ticket-only"
    GRANT_APPROVED_TICKET_ACCOMMODATION = "grant-approved-ticket-accommodation"
    GRANT_APPROVED_TICKET_TRAVEL = "grant-approved-ticket-travel"
    GRANT_APPROVED_TICKET_TRAVEL_ACCOMMODATION = "grant-approved-ticket-travel-accommodation"
    GRANT_REPLY_APPLICANT_NEED_MORE_INFO = "grant-reply-applicant-need-more-info"
    GRANT_WAITING_LIST = "grant-waiting-list"
    GRANT_WAITING_LIST_UPDATE = "grant-waiting-list-update"
    GRANT_VOUCHER_CODE = "grant-voucher-code"
    GRANT_REJECTED = "grant-rejected"

    # Users
    RESET_PASSWORD = "reset-password"

    # Submissions
    SUBMISSION_ACCEPTED = "submission-accepted"
    SUBMISSION_REJECTED = 'submission-rejected'
    SUBMISSION_IN_WAITING_LIST = "submission-in-waiting-list"
    SUBMISSION_SCHEDULE_TIME_CHANGED = "submission-schedule-time-change"
    SPEAKER_VOUCHER_CODE = "speaker-voucher-code"
    SPEAKER_COMMUNICATION = "speaker-communication"

    # Deprecated
    NEW_COMMENT_ON_SUBMISSION = "new-comment-on-submission"
    NEW_SCHEDULE_INVITATION_ANSWER = "new-schedule-invitation-answer"

    def __str__(self) -> str:
        return str.__str__(self)
