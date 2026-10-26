"""Write my latest public GitHub activity between the activity markers in README.md."""
import json
import os
import re
import urllib.request

USER, LIMIT = "ExNNeph", 5

req = urllib.request.Request(f"https://api.github.com/users/{USER}/events/public?per_page=100",
                             headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"})
events = json.load(urllib.request.urlopen(req))

lines, seen = [], set()
for e in events:
    repo, day = e["repo"]["name"], e["created_at"][:10]
    if repo == f"{USER}/{USER}":
        continue
    link = f"[{repo.split('/')[1]}](https://github.com/{repo})"
    if e["type"] == "PushEvent":
        text = f"⬆️ Pushed to {link}"
    elif e["type"] == "PublicEvent":
        text = f"🎉 Published {link}"
    elif e["type"] == "CreateEvent" and e["payload"].get("ref_type") == "repository":
        text = f"🌱 Started {link}"
    else:
        continue
    if (text, day) not in seen:  # one line per action, repo and day
        seen.add((text, day))
        lines.append(f"- {text} · {day}")
    if len(lines) == LIMIT:
        break

readme = open("README.md", encoding="utf-8").read()
block = "<!--START_SECTION:activity-->\n" + "\n".join(lines) + "\n<!--END_SECTION:activity-->"
new = re.sub(r"<!--START_SECTION:activity-->.*?<!--END_SECTION:activity-->", lambda _: block, readme, flags=re.S)
open("README.md", "w", encoding="utf-8").write(new)
