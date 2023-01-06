import time
import requests

# Get a list of Bible verses
response = requests.get("https://www.biblegateway.com/votd/get/?format=json&version=KJV")
data = response.json()
verses = data['votd']['text']
verses = verses.replace("&ldquo;", "")
verses = verses.replace("&rdquo;", "")
verses = verses.replace("&#8220;", "")
scripture = data["votd"]["display_ref"]
date = data['votd']['day'] + "- "+ data['votd']['month']+"- "+ data['votd']['year']
# # Set the message to the verse
# message = verse
print(verses)
print()
print(scripture)
print()
print(date)
print()
print(response.json())
message = f"""
{verses}
{scripture}
{date}
"""
