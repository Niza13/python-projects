import subprocess
import re

def get_wifi_profiles():
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], text=True)
    profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)
    return [p.strip() for p in profiles]

def get_wifi_password(profile_name):
    try:
        output = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'],
            stderr=subprocess.DEVNULL,
            text=True
        )
        password = re.search(r"Key Content\s*:\s(.*)", output)
        return password.group(1).strip() if password else "(No password found)"
    except subprocess.CalledProcessError:
        return "(Access denied or profile not found)"

def main():
    profiles = get_wifi_profiles()

    if not profiles:
        print("No Wi-Fi profiles found.")
        return

    with open("wifi_passwords.txt", "w", encoding="utf-8") as file:
        file.write("📶 Saved Wi-Fi Profiles and Passwords:\n\n")
        print("📶 Saved Wi-Fi Profiles and Passwords:\n")

        for profile in profiles:
            password = get_wifi_password(profile)
            line = f"🔹 {profile}: {password}"
            print(line)
            file.write(line + "\n")

    print("\n✅ Passwords saved to 'wifi_passwords.txt'")

if __name__ == "__main__":
    main()
