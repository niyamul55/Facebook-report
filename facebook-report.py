import random
import time
import os

# User-Agent list
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 Chrome/112.0.5615.138 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; U; Android 10; en-US; SM-A107F) AppleWebKit/537.36 Chrome/99.0.4844.94 Mobile Safari/537.36"
]

# Clear console and open link
os.system('clear')
os.system("xdg-open https://t.me/nhthacker")

print("""
\033[0;36m
Developer: ●▬▬▬▬๑۩🇳‌🇭‌🇹‌۩๑▬▬▬▬๑۩🇭‌🇦‌🇨‌🇰‌🇪‌🇷‌◇۩๑▬▬▬▬●
\033[0m
""")

# Input
fb_id = input("Enter Facebook ID or Link: ").strip()
count_input = input("How many times do you want to report? ").strip()

if not fb_id or not count_input.isdigit() or int(count_input) <= 0:
    print("❌ Please enter a valid Facebook ID/Link and number of reports!")
    exit()

count = int(count_input)
reason = "Unethical activity / spam / abuse"

print(f"\nSimulating sending {count} reports to {fb_id}\n")

# Report simulation
for i in range(count):
    user_agent = random.choice(USER_AGENTS)
    print(f"Report #{i+1}:")
    print(f"  Target Facebook ID/Link: {fb_id}")
    print(f"  Reason: {reason}")
    print(f"  User-Agent: {user_agent}\n")
    print(f"\033[91m{i+1} ✅ report sent successfully\033[0m")
    time.sleep(1)
   