import argparse
import html


def convert_text_to_html(text):
    """
    Converts plain text to HTML, escaping necessary characters and replacing newlines with <br> tags.
    """
    # Escape HTML special characters
    safe_text = html.escape(text)
    # Replace newlines with <br> for HTML display
    html_text = safe_text.replace('\n', '<br>\n')
    # Wrap the text in a basic HTML template
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted Text</title>
</head>
<body>
    <p>{html_text}</p>
</body>
</html>"""


def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Convert text to HTML.")
    parser.add_argument('-f', '--file', type=str, help="Path to the input text file.")
    parser.add_argument('-t', '--text', type=str, help="Direct text input.")
    parser.add_argument('-o', '--output', required=True, type=str, help="Path to the output HTML file.")

    args = parser.parse_args()

    # If text is provided directly, use it; otherwise, read the text from the specified file
    if args.text:
        text = args.text
    elif args.file:
        with open(args.file, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        raise ValueError("No text input provided.")

    # Convert the text to HTML
    html_content = convert_text_to_html(text)

    # Write the HTML content to the specified output file
    with open(args.output, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)


if __name__ == "__main__":
    main()
