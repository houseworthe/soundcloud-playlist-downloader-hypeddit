
# Project Setup Guide

This guide will help you set up Python, Selenium, and ChromeDriver on your system, install the HypedditSkip-V2 extension, and configure your download path for running the provided program.

## Prerequisites

Before you begin, make sure you have administrative access to your system to install software.

## Installing Python

1. **Download Python**: Go to the [official Python website](https://www.python.org/downloads/) and download the latest version for your operating system.
2. **Install Python**: Run the installer. Make sure to check the box that says "Add Python to PATH" during installation.

## Setting Up Selenium

1. **Install Selenium**: Open a command prompt or terminal and run the following command:

   ```sh
   pip install selenium
   ```

## Installing ChromeDriver

1. **Check Chrome Version**: Open Google Chrome, go to `chrome://version/` and check your version.
2. **Download ChromeDriver**: Go to the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/) and download the version of ChromeDriver that corresponds to your version of Chrome.
3. **Extract ChromeDriver**: Unzip the downloaded file to a known directory on your system.

## Installing HypedditSkip-V2 Extension

1. **Download HypedditSkip-V2**: Visit the [HypedditSkip-V2 GitHub repository](https://github.com/JackSibley/HypedditSkip-V2) and download the latest release.
2. **Install the Extension in Chrome**:
   - Open Google Chrome.
   - Go to `chrome://extensions/`.
   - Enable "Developer mode" at the top right.
   - Click "Load unpacked" and select the folder where you unzipped the HypedditSkip-V2 extension.

## Setting Up the File Path

1. **Determine Download Path**: Decide on a download folder where your files will be saved.
2. **Configure Chrome**: In Chrome settings, go to the "Downloads" section and set the download path to your chosen folder.

## Running the Program

1. **Clone/Download This Repository**: Get the project files onto your system.
2. **Open the Program**: Navigate to the project directory in your command prompt or terminal.
3. **Install Dependencies**: Run `pip install -r requirements.txt` to install the required Python packages.
4. **Run the Script**: Execute the script with `python main.py` (100_downloader for hypeddit top charts).
5. **Follow Prompts**: When the script is running, follow the prompts in the terminal. Install the HypedditSkip-V2 extension if you haven't already, set up your download path in Chrome, then return to the terminal or command prompt and press "Enter" to continue.

## Troubleshooting

If you encounter any issues, ensure that all steps have been followed correctly. Check that your Python version is up-to-date, that Selenium has been installed correctly, and that ChromeDriver matches your Chrome version and is placed in a directory included in your system's PATH.

For any additional help, refer to the official documentation for each tool or post an issue in this repository.
