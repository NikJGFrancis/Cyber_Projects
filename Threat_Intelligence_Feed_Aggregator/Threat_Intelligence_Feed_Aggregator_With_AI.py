import requests
import csv
import json
import xml.etree.ElementTree as ET

# ------------------ Configuration ------------------
feeds = [
    {"name": "Feed1_JSON", "url": "https://example.com/threats.json", "type": "json"},
    {"name": "Feed2_XML", "url": "https://example.com/threats.xml", "type": "xml"}
]
output_file = "threat_intelligence.csv"


# ------------------ Functions ------------------
def fetch_feed(feed):
    """Fetch raw data from a threat intelligence feed."""
    response = requests.get(feed["url"])
    if response.status_code == 200:
        return response.text
    else:
        print(f"⚠️ Failed to fetch {feed['name']}: {response.status_code}")
        return None


def parse_feed(feed, raw_data):
    """Parse feed data depending on format (JSON or XML)."""
    parsed_data = []

    if feed["type"] == "json":
        try:
            data = json.loads(raw_data)
            for item in data.get("threats", []):
                parsed_data.append({
                    "Source": feed["name"],
                    "Indicator": item.get("indicator"),
                    "Type": item.get("type"),
                    "Severity": item.get("severity")
                })
        except Exception as e:
            print(f"Error parsing JSON feed {feed['name']}: {e}")

    elif feed["type"] == "xml":
        try:
            root = ET.fromstring(raw_data)
            for threat in root.findall(".//threat"):
                parsed_data.append({
                    "Source": feed["name"],
                    "Indicator": threat.findtext("indicator"),
                    "Type": threat.findtext("type"),
                    "Severity": threat.findtext("severity")
                })
        except Exception as e:
            print(f"Error parsing XML feed {feed['name']}: {e}")

    return parsed_data


def highlight_critical(threats):
    """Highlight the most critical threats based on severity."""
    critical = [t for t in threats if str(t["Severity"]).lower() in ("high", "critical", "severe")]
    return critical


def save_to_csv(threats, filename):
    """Save merged threat intelligence data into a CSV file."""
    fieldnames = ["Source", "Indicator", "Type", "Severity"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(threats)


# ------------------ Main Logic ------------------
all_threats = []

for feed in feeds:
    raw_data = fetch_feed(feed)
    if raw_data:
        parsed = parse_feed(feed, raw_data)
        all_threats.extend(parsed)

critical_threats = highlight_critical(all_threats)

save_to_csv(all_threats, output_file)

print(f"✅ Aggregated {len(all_threats)} threats from {len(feeds)} feeds.")
print(f"🚨 Found {len(critical_threats)} critical threats. Report saved to {output_file}.")
