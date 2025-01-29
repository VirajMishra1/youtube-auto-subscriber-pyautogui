import time
import pyautogui
import webbrowser
from screeninfo import get_monitors


def load_channels(file_path):
    """Loads YouTube channel links from a file."""
    try:
        with open(file_path, 'r') as file:
            channels = [channel.strip() for channel in file.readlines()]
            print(f"Loaded {len(channels)} channels.")
            return channels
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def handle_multiple_monitors(channel_urls):
    """Handles automation for multiple monitors."""
    monitors = get_monitors()
    print(f"Detected {len(monitors)} monitor(s).")

    for i, channel_url in enumerate(channel_urls):
        for m in monitors:
            print(f"Processing on monitor: {m}")

            # Open the YouTube channel
            webbrowser.open(channel_url)
            time.sleep(2)  # Adjust for page load time

            # Adjust coordinates dynamically for different monitor resolutions
            width_ratio = m.width / 1512
            height_ratio = m.height / 982

            # Move to "Subscribe" button (coordinates adjusted for scaling)
            pyautogui.moveTo(1298 * width_ratio, 380 * height_ratio, duration=8)
            pyautogui.click()

            # Close the tab
            pyautogui.moveTo(471 * width_ratio, 24 * height_ratio, duration=2)
            pyautogui.click()

            print(f"Subscribed to {channel_url}.")

        # Stop after processing all channels
        if i == len(channel_urls) - 1:
            print("All channels processed.")
            return


def main():
    # File containing the list of YouTube channels
    file_path = "path_to_your_channel_list.txt"

    # Load channel URLs
    channel_urls = load_channels(file_path)
    if not channel_urls:
        print("No channels to process. Exiting.")
        exit(1)

    print("Make sure you are logged into YouTube before starting this script.")
    input("Press Enter to continue after logging in...")

    # Handle automation for all monitors
    handle_multiple_monitors(channel_urls)


if __name__ == "__main__":
    main()
