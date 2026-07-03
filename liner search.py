def is_spam(sender_id, blacklist):
    """
    Performs a linear search to check if sender_id is in the blacklist.
    """
    for email in blacklist:
        if email == sender_id:
            return True  # Found in blacklist (Spam)
    return False  # Not found (Safe)

# Example Usage
blacklist_emails = ["spammer123@xyz.com", "fake_deals@promo.org", "scam_bot@malware.net"]
incoming_email = "fake_deals@promo.org"

print("--- 1. Spam Detector ---")
if is_spam(incoming_email, blacklist_emails):
    print(f"ALERT: {incoming_email} is flagged as SPAM!")
else:
    print(f"SAFE: {incoming_email} is clean.")
