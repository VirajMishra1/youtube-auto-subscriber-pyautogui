# YouTube Auto-Subscriber Bot (PyAutoGUI) 🎥

## Project Description

The **YouTube Auto-Subscriber Bot (PyAutoGUI)** is a Python-based script that automates subscribing to YouTube channels. This tool leverages `pyautogui` for GUI automation to simulate mouse movements and clicks. It detects your screen resolution, opens YouTube channels in your default browser, and subscribes to them if the resolution matches predefined settings.

## 🚀 Features

1. **Automated Channel Subscription**: Opens YouTube channels from a list and clicks the subscribe button.
2. **Dynamic Screen Resolution Detection**: Checks for a compatible single-monitor resolution before running.
3. **Browser Automation**: Automatically opens URLs in the default web browser.
4. **Headless Execution**: Simulates user actions on the screen using `pyautogui`.
5. **Error Handling**: Gracefully handles incompatible screen resolutions or multi-monitor setups.

## 🔧 Technologies Used

- **Python**: Core programming language.
- **PyAutoGUI**: For simulating mouse movements and clicks.
- **Webbrowser**: To open URLs in the default web browser.
- **Screeninfo**: For monitor resolution detection.

## 📦 Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd youtube-auto-subscriber-pyautogui
    ```
3. **Install Required Dependencies**:
    ```bash
    pip install pyautogui screeninfo
    ```

4. **Edit Configuration**:
    - Update the `channel_urls` list in the script with the YouTube channel URLs you want to subscribe to:
      ```python
      channel_urls = [
          'https://www.youtube.com/c/YesTheory',
          'https://www.youtube.com/c/YungChip',
          'https://www.youtube.com/zerkaa'
      ]
      ```

5. **Run the Script**:
    ```bash
    python youtube_auto_subscriber.py
    ```

## 🔹 Usage

1. Ensure your monitor resolution matches the supported dimensions (1512x982 by default).
2. Prepare a list of YouTube channel URLs and update the script.
3. Run the script, and it will:
    - Open each URL in your browser.
    - Simulate mouse movements and clicks to subscribe to the channel.
4. The script skips multi-monitor setups or incompatible resolutions.

## 📚 Example

### Sample Output:
```
Detected Monitor: Monitor(x=0, y=0, width=1512, height=982)
Compatible monitor resolution detected. Starting automation...
Subscribed to https://www.youtube.com/c/YesTheory
Subscribed to https://www.youtube.com/c/YungChip
Subscribed to https://www.youtube.com/zerkaa
Subscription process completed!
```

### Incompatible Resolution:
```
Detected Monitor: Monitor(x=0, y=0, width=1920, height=1080)
Incompatible monitor resolution. Adjust your screen settings and try again.
```

## 🛡️ Security Note

- This script uses `pyautogui`, which relies on precise mouse coordinates. Ensure your browser and screen setup match the expected layout.
- Avoid running the script in environments with sensitive information on the screen.

## 🤝 Contribution

Contributions are welcome! If you have ideas for improving the project, feel free to fork the repository and submit a pull request.

## 🖋️ License

This project is licensed under the MIT License.

## 👨‍💻 Author

Viraj Mishra

