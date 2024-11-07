# File Downloader GUI

This is a simple graphical user interface (GUI) application built with `tkinter` that allows users to download files from a URL to their local machine. The application handles input validation, error handling, and provides feedback on download success or failure.

## Features

- **GUI for Ease of Use:** A straightforward and easy-to-use interface built with tkinter, which allows users to input a URL and a filename.
- **File Downloading:** Users can download content from any valid URL (e.g., an image, PDF, or any other file) and save it to a specified file on their local machine.
- **Error Handling:** The app handles errors such as empty inputs and issues during downloading (e.g., network errors or invalid URLs) with informative error messages.
- **Success Feedback:** After a successful download, the app shows a message confirming that the content was downloaded and saved successfully.

## Libraries Used

- **tkinter:** Provides the GUI components for creating the window, labels, entry fields, and buttons.
- **requests:** Used for making HTTP requests to the URL and downloading the content.

## Code Explanation

### Functions:

#### `download_content()`
- Retrieves the URL and filename from the user input fields.
- If either input is missing, an error message is shown using messagebox.
- The function then attempts to download the content from the specified URL using `requests.get()`.
- If the download is successful, the content is saved to the specified filename. If any error occurs (e.g., network issues or invalid URL), an error message is shown.
- Upon successful download, the app shows a confirmation message with the filename.

### Tkinter GUI Components:

- **url_label:** A label prompting the user to enter the URL.
- **url_entry:** An entry widget for the user to input the URL from which content will be downloaded.
- **filename_label:** A label prompting the user to enter the filename to save the content.
- **filename_entry:** An entry widget for the user to specify the filename where the downloaded content will be saved.
- **download_button:** A button that initiates the downloading process by calling the `download_content` function when clicked.

### Error Handling:

- The app checks if both the URL and filename fields are filled. If either is empty, it displays an error message.
- In case of download failure (e.g., invalid URL, network issues), the app catches the exception and shows an error message using `messagebox.showerror`.

### User Experience:

- Once the user provides the URL and filename, clicking the "Download" button starts the download process.
- If the download is successful, a success message appears, informing the user of the successful content download.
- In case of an error, the app displays a relevant error message to guide the user.

### Window Configuration:

- The main window is created with the `Tk()` class, with a title and fixed window size (400x200).
- The background color of the window is set to white, and the window layout is configured using `pack()` for proper placement of each widget.

## Installation

To use the file downloader, you need to have Python 3 and the required libraries installed.

1. Clone or download this repository to your local machine.
2. Install the required libraries using the following command:

    ```bash
    pip install tkinter requests
    ```

3. Run the script to launch the application:

    ```bash
    python file_downloader.py
    ```

## Thank You

Thank you for using the File Downloader GUI! We hope this tool makes your file downloading tasks easier and more efficient.

