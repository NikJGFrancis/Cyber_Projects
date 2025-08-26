Threat Intelligence Feed Aggregator

A Python script that collects threat intelligence data from multiple feeds (JSON & XML), parses the results, and aggregates them into a **CSV report**.
It also highlights **critical threats** based on severity levels (e.g., *High, Critical, Severe*).

Useful for **cybersecurity analysts, SOC teams, and researchers** who need to consolidate threat data for monitoring or further analysis.

Features

* Fetches threat data from **multiple feeds** (JSON or XML).
* Normalizes and merges all feeds into a **single CSV file**.
* Highlights **critical threats** by severity.
* Easily extendable to support new feeds and formats.

Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/threat-intel-aggregator.git
   cd threat-intel-aggregator
   ```

2. Install dependencies:

   ```bash
   pip install requests
   ```

3. Update the `feeds` list in the script with your feed sources:

   ```python
   feeds = [
       {"name": "Feed1_JSON", "url": "https://example.com/threats.json", "type": "json"},
       {"name": "Feed2_XML", "url": "https://example.com/threats.xml", "type": "xml"}
   ]
   ```

4. Run the script:

   ```bash
   python3 threat_aggregator.py
   ```

Example Output

Console Output

```
✅ Aggregated 45 threats from 2 feeds.
🚨 Found 8 critical threats. Report saved to threat_intelligence.csv.
```

CSV Report (`threat_intelligence.csv`)

| Source      | Indicator       | Type     | Severity |
| ----------- | --------------- | -------- | -------- |
| Feed1\_JSON | 192.168.1.100   | IP       | High     |
| Feed1\_JSON | evil-domain.com | Domain   | Critical |
| Feed2\_XML  | badfile.exe     | FileHash | Medium   |
| Feed2\_XML  | 203.0.113.55    | IP       | Severe   |

Customization

* Add new feeds by appending them to the `feeds` list.
* Extend parsing logic in `parse_feed()` to support new data formats.
* Modify `highlight_critical()` if you use different severity scales.

License

This project is licensed under the MIT License.
