import os
import sys
from bs4 import BeautifulSoup
import html2text
import requests


def fetch_cses_problem(url, category_folder):
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
      )
  }
  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print(f"❌ Failed to fetch URL. Status code: {response.status_code}")
    return

  soup = BeautifulSoup(response.text, "html.parser")

  # Extract problem title
  title_tag = soup.find("h1")
  if not title_tag:
    print("❌ Could not find problem title.")
    return
  title = title_tag.text.strip()

  # Extract problem content block
  content_div = soup.find("div", class_="content")
  if not content_div:
    print("❌ Could not find problem content.")
    return

  # Convert HTML content to Markdown
  h = html2text.HTML2Text()
  h.ignore_links = False
  markdown_content = h.handle(str(content_div))

  # Sanitize title for safe directory naming
  safe_title = "".join(
      c if c.isalnum() or c in (" ", "-", "_") else "" for c in title
  ).strip()

  # Create path directly inside the existing category folder
  folder_name = os.path.join(category_folder, safe_title)
  os.makedirs(folder_name, exist_ok=True)

  # Save README.md with the description
  readme_path = os.path.join(folder_name, "README.md")
  with open(readme_path, "w", encoding="utf-8") as f:
    f.write(f"# {title}\n\n")
    f.write(f"**Link:** [{url}]({url})\n\n---\n\n")
    f.write(markdown_content)

  # Create a clean template solution.py file optimized for CSES input handling
  code_path = os.path.join(folder_name, "solution.py")
  if not os.path.exists(code_path):
    with open(code_path, "w", encoding="utf-8") as f:
      f.write(f"# CSES Problem: {title}\n")
      f.write(f"# URL: {url}\n\n")
      f.write("import sys\n\n\ndef solve():\n")
      f.write("    # Fast I/O: reads all tokens from stdin efficiently\n")
      f.write("    input_data = sys.stdin.read().split()\n")
      f.write("    if not input_data:\n")
      f.write("        return\n")
      f.write("    \n")
      f.write("    n = int(input_data[0])\n")
      f.write("    # TODO: Write your solution logic here\n\n\n")
      f.write("if __name__ == '__main__':\n")
      f.write("    solve()\n")

  print(f"✅ Successfully generated files for: '{title}'")
  print(f"📁 Path: {folder_name}")


if __name__ == "__main__":
  if len(sys.argv) < 3:
    print(
        "Usage: python get_cses.py <cses_url>"
        " <existing_category_folder>"
    )
    print(
        "Example: python get_cses.py https://cses.fi/problemset/task/1068"
        " Introductory-Problems"
    )
  else:
    fetch_cses_problem(sys.argv[1], sys.argv[2])