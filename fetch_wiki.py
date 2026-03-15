import urllib.request
import json
import os
import time

items = {
  "Kanchipuram_Silk_Saree": "Sari",
  "Banarasi_Zari_Saree": "Banarasi_sari",
  "Premium_Cotton_Saree": "Textile_arts_of_Bangladesh",
  "Handloom_Cotton_Shirt": "Khadi",
  "Pure_Silk_Dhoti_Set": "Dhoti",
  "Wedding_Silk_Kurta": "Kurta",
  "Chanderi_Suit_Material": "Chanderi_sari",
  "Embroidered_Fabric_Set": "Embroidery_of_India",
  "Cotton_Bedspread_Set": "Bed_sheet",
  "Egyptian_Cotton_Towels": "Towel",
  "Mysore_Silk_Special": "Mysore_silk",
  "Pashmina_Winter_Shawl": "Pashmina",
  "Mens_Wedding_Sherwani": "Sherwani",
  "Chettinad_Cotton_Saree": "Sari",  # fallbacks
  "Designer_Anarkali_Suit": "Anarkali_Salwar_Suit",
  "Velvet_Bedspread": "Velvet"
}

out_dir = os.path.join("public", "images")
os.makedirs(out_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (RayanBot/1.0)'}

for filename, wiki_title in items.items():
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&pithumbsize=800&titles={wiki_title}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            pages = data['query']['pages']
            page = list(pages.values())[0]
            if 'thumbnail' in page:
                img_url = page['thumbnail']['source']
                # Download image
                filepath = os.path.join(out_dir, filename + '.jpg')
                img_req = urllib.request.Request(img_url, headers=headers)
                with urllib.request.urlopen(img_req) as img_res:
                    with open(filepath, 'wb') as f:
                        f.write(img_res.read())
                print(f"Success: Downloaded {filename} from {wiki_title}")
            else:
                print(f"Failed: No image found for {wiki_title}")
    except Exception as e:
        print(f"Failed for {wiki_title}: {e}")
    time.sleep(1)
