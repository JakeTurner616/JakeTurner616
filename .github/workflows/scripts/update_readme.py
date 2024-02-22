import feedparser
import re

# Parse the Atom feed
feed = feedparser.parse('https://serverboi.org/feed.xml')

# Prepare the markdown content
new_content = '\n'.join([f"- {entry.published[:10]} - [{entry.title}]({entry.link})" for entry in feed.entries[:5]])  # Adjust the slicing as needed

# Read the current README
readme_path = 'README.md'
with open(readme_path, 'r', encoding='utf-8') as file:
    readme_content = file.read()

# Replace the content between the feed start and end comments
updated_readme_content = re.sub(r'<!-- feed start -->.*<!-- feed end -->', f'<!-- feed start -->\n{new_content}\n<!-- feed end -->', readme_content, flags=re.DOTALL)

# Write back the updated README
with open(readme_path, 'w', encoding='utf-8') as file:
    file.write(updated_readme_content)
