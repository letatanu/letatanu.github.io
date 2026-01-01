from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os

# 1. Set up Proxy Generator
pg = ProxyGenerator()

if 'SCRAPER_API_KEY' in os.environ:
    # Use ScraperAPI if the key works (Reliable)
    success = pg.ScraperAPI(os.environ['SCRAPER_API_KEY'])
else:
    # Fallback to free proxies (Unreliable, but worth a try if no key)
    print("No SCRAPER_API_KEY found. Attempting to use Free Proxies...")
    success = pg.FreeProxies()

if not success:
    print("Failed to set up a proxy. Google Scholar may block the request.")
else:
    scholarly.use_proxy(pg)

# 2. Fetch Author Data
# We wrap this in a try-except block to catch blocking errors gracefully
try:
    author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

    # 3. Update Data
    name = author['name']
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']:v for v in author['publications']}
    print(json.dumps(author, indent=2))

    # 4. Save Results
    os.makedirs('results', exist_ok=True)
    with open(f'results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
      "schemaVersion": 1,
      "label": "citations",
      "message": f"{author['citedby']}",
    }
    with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

except Exception as e:
    print(f"Error fetching data: {e}")
    # Re-raise to mark the GitHub Action as failed
    raise e