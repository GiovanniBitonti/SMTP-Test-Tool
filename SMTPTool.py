import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

# Function to test SMTP connection
def test_smtp_connection():
    smtp_server = smtp_server_entry.get()
    smtp_port = int(smtp_port_entry.get())
    sender_email = sender_email_entry.get()
    recipient_email = recipient_email_entry.get()
    smtp_user = smtp_user_entry.get()
    smtp_password = smtp_password_entry.get()

    try:
        log_output.delete(1.0, tk.END)  # Clear previous output
        log_output.insert(tk.END, "---- Starting SMTP test ----\n\n")
        log_output.insert(tk.END, f"Connecting to SMTP server: {smtp_server} on port: {smtp_port}\n\n")

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "SMTP Test"
        body = "This is a test email to confirm SMTP connection."
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        log_output.insert(tk.END, "✔️ TLS connection established.\n\n", "success")

        # Log in if credentials are provided
        if smtp_user and smtp_password:
            log_output.insert(tk.END, f"Logging in as: {smtp_user}\n\n")
            try:
                server.login(smtp_user, smtp_password)
                log_output.insert(tk.END, "✔️ Login successful.\n\n", "success")
            except smtplib.SMTPAuthenticationError as e:
                log_output.insert(tk.END, f"❌ Authentication failed: {e}\n", "error")
                log_output.insert(tk.END, "Possible cause: Incorrect username or password, or security settings on the email account.\n\n")
                return
            except Exception as e:
                log_output.insert(tk.END, f"❌ Error during login: {e}\n\n", "error")
                return

        # Send the email
        log_output.insert(tk.END, f"Sending email from {sender_email} to {recipient_email}...\n\n")
        try:
            server.sendmail(sender_email, recipient_email, msg.as_string())
            log_output.insert(tk.END, "✔️ Email sent successfully!\n\n", "success")
        except smtplib.SMTPRecipientsRefused as e:
            log_output.insert(tk.END, f"❌ Error: Recipient address refused. Details: {e}\n", "error")
            log_output.insert(tk.END, "Possible cause: Invalid recipient email address.\n\n")
        except smtplib.SMTPSenderRefused as e:
            log_output.insert(tk.END, f"❌ Error: Sender address refused. Details: {e}\n", "error")
            log_output.insert(tk.END, "Possible cause: Invalid sender email address.\n\n")
        except smtplib.SMTPDataError as e:
            log_output.insert(tk.END, f"❌ Error: The SMTP server refused to accept the message data. Details: {e}\n", "error")
            log_output.insert(tk.END, "Possible cause: The email content might be invalid or too large.\n\n")
        except Exception as e:
            log_output.insert(tk.END, f"❌ Error during email sending: {e}\n\n", "error")

        server.quit()
        log_output.insert(tk.END, "✔️ SMTP connection closed.\n\n", "success")
        log_output.insert(tk.END, "---- SMTP test completed ----\n\n")

    except smtplib.SMTPConnectError as e:
        log_output.insert(tk.END, f"❌ Error: Unable to connect to the SMTP server {smtp_server}. Details: {e}\n", "error")
        log_output.insert(tk.END, "Possible cause: Incorrect SMTP server or port, or network issues.\n\n")
    except smtplib.SMTPServerDisconnected as e:
        log_output.insert(tk.END, f"❌ Error: Disconnected unexpectedly from the SMTP server. Details: {e}\n", "error")
        log_output.insert(tk.END, "Possible cause: Network issues or the server might have timed out.\n\n")
    except Exception as e:
        log_output.insert(tk.END, f"❌ An unexpected error occurred: {e}\n\n", "error")


# Creating the UI
root = tk.Tk()
root.title("SMTP Tester")
root.geometry("460x800")  # Adjusted window size
root.resizable(False, False)  # Prevent resizing of the window
root.configure(bg="#F7F7F7")  # Light background for a modern look

# Style configurations
label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 10)
button_font = ("Arial", 12, "bold")

# Apply rounded corners and modern colors
entry_bg = "#E0E0E0"
entry_fg = "#000000"
button_bg = "#4CAF50"
button_fg = "#FFFFFF"
log_bg = "#F0F0F0"
log_fg = "#000000"

# Labels and entry fields with rounded corners
def rounded_entry(parent, **kwargs):
    entry = tk.Entry(parent, **kwargs)
    entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=1, bd=5, relief="flat")
    return entry

tk.Label(root, text="SMTP Server:", font=label_font, bg="#F7F7F7").pack(pady=5)
smtp_server_entry = rounded_entry(root, width=50, font=entry_font, bg=entry_bg, fg=entry_fg)
smtp_server_entry.pack(pady=5)

tk.Label(root, text="SMTP Port:", font=label_font, bg="#F7F7F7").pack(pady=5)
smtp_port_entry = rounded_entry(root, width=50, font=entry_font, bg=entry_bg, fg=entry_fg)
smtp_port_entry.pack(pady=5)

tk.Label(root, text="Sender Email:", font=label_font, bg="#F7F7F7").pack(pady=5)
sender_email_entry = rounded_entry(root, width=50, font=entry_font, bg=entry_bg, fg=entry_fg)
sender_email_entry.pack(pady=5)

tk.Label(root, text="Recipient Email:", font=label_font, bg="#F7F7F7").pack(pady=5)
recipient_email_entry = rounded_entry(root, width=50, font=entry_font, bg=entry_bg, fg=entry_fg)
recipient_email_entry.pack(pady=5)

tk.Label(root, text="SMTP Username:", font=label_font, bg="#F7F7F7").pack(pady=5)
smtp_user_entry = rounded_entry(root, width=50, font=entry_font, bg=entry_bg, fg=entry_fg)
smtp_user_entry.pack(pady=5)

tk.Label(root, text="SMTP Password:", font=label_font, bg="#F7F7F7").pack(pady=5)
smtp_password_entry = rounded_entry(root, show="*", width=50, font=entry_font, bg=entry_bg, fg=entry_fg)
smtp_password_entry.pack(pady=5)

# Button to run the SMTP test, with rounded corners
test_button = tk.Button(root, text="Run SMTP Test", font=button_font, bg=button_bg, fg=button_fg, command=test_smtp_connection)
test_button.pack(pady=20)
test_button.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=1, bd=5, relief="flat")

# Output log box with rounded edges
tk.Label(root, text="Log Output:", font=label_font, bg="#F7F7F7").pack()
log_output = tk.Text(root, height=10, width=60, font=entry_font, bg=log_bg, fg=log_fg, bd=5, relief="flat")
log_output.pack(pady=5)

# Adding tags to color success and error messages
log_output.tag_config("success", foreground="green")
log_output.tag_config("error", foreground="red")

# Footer
footer = tk.Label(root, text="SMTP Test Tool v1 - Developed by Giovanni Bitonti", bg="#F7F7F7", font=("Arial", 10, "italic"))
footer.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
