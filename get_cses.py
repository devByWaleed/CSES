import os
import sys
import zipfile
from bs4 import BeautifulSoup
import html2text
import requests


def fetch_cses_problem(url, category_folder, zip_path=None):
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

    title_tag = soup.find("h1")
    if not title_tag:
        print("❌ Could not find problem title.")
        return
    title = title_tag.text.strip()

    content_div = soup.find("div", class_="content")
    if not content_div:
        print("❌ Could not find problem content.")
        return

    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown_content = h.handle(str(content_div))

    safe_title = "".join(
        c if c.isalnum() or c in (" ", "-", "_") else "" for c in title
    ).strip()

    folder_name = os.path.join(category_folder, safe_title)
    os.makedirs(folder_name, exist_ok=True)

    readme_path = os.path.join(folder_name, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Link:** [{url}]({url})\n\n---\n\n")
        f.write(markdown_content)

    code_path = os.path.join(folder_name, "solution.py")
    if not os.path.exists(code_path):
        with open(code_path, "w", encoding="utf-8") as f:
            f.write(f"# CSES Problem: {title}\n")
            f.write(f"# URL: {url}\n\n")
            f.write("import sys\n\n\ndef solve():\n")
            f.write("    input_data = sys.stdin.read().split()\n")
            f.write("    if not input_data:\n")
            f.write("        return\n\n")
            f.write("    n = int(input_data[0])\n")
            f.write("    # TODO: Write your solution logic here\n\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    solve()\n")

    if zip_path and os.path.exists(zip_path):
        tests_folder = os.path.join(folder_name, "tests")
        os.makedirs(tests_folder, exist_ok=True)
        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(tests_folder)
            print(f"✅ Extracted test cases into: {tests_folder}")
        except Exception as e:
            print(f"❌ Failed to extract zip file: {e}")
    elif zip_path:
        print(f"⚠️ Warning: Provided zip file path '{zip_path}' does not exist.")

    print(f"✅ Successfully generated files for: '{title}'")
    print(f"📁 Path: {folder_name}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python get_cses.py <cses_url> <existing_category_folder>"
            " [path_to_tests_zip]"
        )
    else:
        zip_file = sys.argv[3] if len(sys.argv) > 3 else None
        fetch_cses_problem(sys.argv[1], sys.argv[2], zip_file)


# Just change "Link" and "Folder Name" as per need
# python get_cses.py https://cses.fi/problemset/task/1083 Introductory-Problems tests.zip