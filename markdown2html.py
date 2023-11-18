import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        sys.exit(1)

    # Extract file names from arguments
    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(md_file):
        sys.exit(1)

    # Read Markdown content and convert to HTML
    with open(md_file, 'r') as md:
        markdown_content = md.read()
        html_content = markdown.markdown(markdown_content)

    # Write HTML content to output file
    with open(html_file, 'w') as html:
        html.write(html_content)

if __name__ == "__main__":
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
    sys.exit(0)

