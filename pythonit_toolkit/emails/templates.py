from enum import Enum


class EmailTemplate(str, Enum):
    GRANT_APPROVED_TICKET_ONLY = "grant-approved-ticket-only"
    GRANT_APPROVED_TICKET_ACCOMMODATION = "grant-approved-ticket-accommodation"
    GRANT_APPROVED_TICKET_TRAVEL = "grant-approved-ticket-travel"
    GRANT_APPROVED_TICKET_TRAVEL_ACCOMMODATION = "grant-approved-ticket-travel-accommodation"
    GRANT_REPLY_APPLICANT_NEED_MORE_INFO = "grant-reply-applicant-need-more-info"
    GRANT_WAITING_LIST = "grant-waiting-list"
    GRANT_REJECTED = "grant-rejected"
    RESET_PASSWORD = "reset-password"
    NEW_COMMENT_ON_SUBMISSION = "new-comment-on-submission"
    SUBMISSION_ACCEPTED = "submission-accepted"
    NEW_SCHEDULE_INVITATION_ANSWER = "new-schedule-invitation-answer"
    SUBMISSION_SCHEDULE_TIME_CHANGED = "submission-schedule-time-change"
    SPEAKER_VOUCHER_CODE = "speaker-voucher-code"
    SPEAKER_COMMUNICATION = "speaker-communication"

    def __str__(self) -> str:
        return str.__str__(self)
