Added Features:
More Detailed Error Handling:

If there’s an authentication issue, the script will log specific errors like wrong username or password.
Specific exceptions are logged for:
Connection failures (SMTPConnectError).
Authentication failures (SMTPAuthenticationError).
Issues with recipient address, sender address, or message data (SMTPRecipientsRefused, SMTPSenderRefused, SMTPDataError).
General errors during login or email sending.
Clear Messaging:

If something goes wrong at any point, you’ll now get clear messages in the terminal indicating what the potential problem is, such as incorrect credentials, connectivity issues, or email formatting problems.