# Reddit Thread to HTML Converter

This Python script fetches a Reddit thread and converts it into a clean, readable HTML document. It uses the PRAW library to interact with the Reddit API and BeautifulSoup for HTML formatting.

## Requirements

- Python 3.x
- PRAW library (`pip install praw`)
- BeautifulSoup library (`pip install beautifulsoup4`)

## Usage

1. Install the required libraries:

```bash
pip install praw beautifulsoup4
```

2. Obtain Reddit API credentials by creating a new application on the [Reddit Developer Portal](https://www.reddit.com/prefs/apps).

3. Replace 'YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET', and 'YOUR_USER_AGENT' in `main.py` with your Reddit API credentials.

4. Run the script:

```bash
python main.py
```

5. Enter the Reddit thread URL when prompted.

6. The script will generate an HTML file named 'reddit_thread.html' with formatted content.

## Output

The generated HTML file includes proper indentation, padding, and color for each comment, displaying the username, score, and content in a clean format.

## Saving as PDF

To save the HTML file as a PDF through your web browser:

1. Open the 'reddit_thread.html' file using your preferred web browser.
2. Navigate to the browser's print option (usually found in the browser menu or using `Ctrl+P` / `Cmd+P`).
3. In the print dialog, choose 'Save as PDF' as the destination.
4. Adjust any print settings if needed and click 'Save' to save the HTML file as a PDF.

Feel free to customize the HTML styles in the script according to your preferences.

## Notes

- Make sure to keep your Reddit API credentials secure and avoid sharing them.
- The script currently generates a simple HTML structure. You can enhance or modify the formatting based on your requirements.
- For any issues or improvements, feel free to open an issue or submit a pull request.

