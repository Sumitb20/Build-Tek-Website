import os
import glob
import re
import json
from html.parser import HTMLParser

class SimpleHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta = []
        self.h1 = []
        self.in_h1 = False
        self.h2 = []
        self.in_h2 = False
        self.h3 = []
        self.in_h3 = False
        self.canonical = ""
        self.images = []
        self.links = []
        self.scripts = []
        self.has_jsonld = False
        self.jsonld_scripts = []
        self.in_jsonld = False
        self.curr_jsonld = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            self.meta.append(attrs_dict)
        elif tag == "link":
            if attrs_dict.get("rel") == "canonical":
                self.canonical = attrs_dict.get("href", "")
        elif tag == "h1":
            self.in_h1 = True
        elif tag == "h2":
            self.in_h2 = True
        elif tag == "h3":
            self.in_h3 = True
        elif tag == "img":
            self.images.append(attrs_dict)
        elif tag == "a":
            if "href" in attrs_dict:
                self.links.append(attrs_dict["href"])
        elif tag == "script":
            if attrs_dict.get("type") == "application/ld+json":
                self.in_jsonld = True
                self.has_jsonld = True
            elif "src" in attrs_dict:
                self.scripts.append(attrs_dict["src"])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False
        elif tag == "h2":
            self.in_h2 = False
        elif tag == "h3":
            self.in_h3 = False
        elif tag == "script" and self.in_jsonld:
            self.in_jsonld = False
            if self.curr_jsonld.strip():
                self.jsonld_scripts.append(self.curr_jsonld.strip())
            self.curr_jsonld = ""

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_h1:
            self.h1.append(data.strip())
        elif self.in_h2:
            self.h2.append(data.strip())
        elif self.in_h3:
            self.h3.append(data.strip())
        elif self.in_jsonld:
            self.curr_jsonld += data

site_dir = "/home/sumit/.gemini/antigravity-ide/scratch/BuildTek-Website"
results = {}

for html_file in sorted(glob.glob(os.path.join(site_dir, "*.html"))):
    fname = os.path.basename(html_file)
    with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    parser = SimpleHTMLParser()
    try:
        parser.feed(content)
    except Exception as e:
        pass
    
    desc = ""
    robots = ""
    for m in parser.meta:
        if m.get("name", "").lower() == "description":
            desc = m.get("content", "")
        if m.get("name", "").lower() == "robots":
            robots = m.get("content", "")

    # Validate JSON-LD
    jsonld_valid = True
    jsonld_errors = []
    for j in parser.jsonld_scripts:
        try:
            json.loads(j)
        except Exception as err:
            jsonld_valid = False
            jsonld_errors.append(str(err))

    results[fname] = {
        "title": parser.title.strip(),
        "description": desc.strip(),
        "canonical": parser.canonical,
        "robots": robots,
        "h1_count": len(parser.h1),
        "h1s": [x for x in parser.h1 if x],
        "has_jsonld": parser.has_jsonld,
        "jsonld_valid": jsonld_valid,
        "jsonld_errors": jsonld_errors,
        "images_count": len(parser.images),
        "missing_alt": [img.get("src", "") for img in parser.images if not img.get("alt")],
        "size_kb": round(len(content) / 1024, 1)
    }

print(json.dumps(results, indent=2))
with open("/home/sumit/.gemini/antigravity-ide/scratch/BuildTek-Website/scratch/initial_audit_results.json", "w") as out:
    json.dump(results, out, indent=2)
