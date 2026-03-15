import os
import urllib.request
import time

images = [
  {"name": "Kanchipuram Silk Saree", "url": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=600&q=80"},
  {"name": "Banarasi Zari Saree", "url": "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?w=600&q=80"},
  {"name": "Premium Cotton Saree", "url": "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=600&q=80"},
  {"name": "Handloom Cotton Shirt", "url": "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=600&q=80"},
  {"name": "Pure Silk Dhoti Set", "url": "https://images.unsplash.com/photo-1611601679655-7c8bc197f0c6?w=600&q=80"},
  {"name": "Wedding Silk Kurta", "url": "https://images.unsplash.com/photo-1597113366853-9a93ad3f1002?w=600&q=80"},
  {"name": "Chanderi Suit Material", "url": "https://images.unsplash.com/photo-1593030761757-71fae45fa0e7?w=600&q=80"},
  {"name": "Embroidered Fabric Set", "url": "https://images.unsplash.com/photo-1589310243389-96a5483213a8?w=600&q=80"},
  {"name": "Cotton Bedspread Set", "url": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=600&q=80"},
  {"name": "Egyptian Cotton Towels", "url": "https://images.unsplash.com/photo-1560064060-1f0124976cae?w=600&q=80"},
  {"name": "Mysore Silk Special", "url": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=600&q=80"},
  {"name": "Pashmina Winter Shawl", "url": "https://images.unsplash.com/photo-1520903920243-00d872a2d1c9?w=600&q=80"},
  {"name": "Mens Wedding Sherwani", "url": "https://images.unsplash.com/photo-1623091410901-00e2d268901f?w=600&q=80"},
  {"name": "Chettinad Cotton Saree", "url": "https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=600&q=80"},
  {"name": "Designer Anarkali Suit", "url": "https://images.unsplash.com/photo-1584483733075-8bd3624dfdf2?w=600&q=80"},
  {"name": "Velvet Bedspread", "url": "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=600&q=80"}
]

out_dir = os.path.join("public", "images")
os.makedirs(out_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}

for img in images:
    name_fmt = img['name'].replace(' ', '_') + '.jpg'
    filepath = os.path.join(out_dir, name_fmt)
    print(f"Downloading {name_fmt}...")
    try:
        req = urllib.request.Request(img['url'], headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        print(f"Success: {name_fmt}")
    except Exception as e:
        print(f"Failed {name_fmt}: {e}")
        # fallback to a placeholder if it really fails
        pass
    time.sleep(1) # sleep to prevent rate limiting
