const fs = require('fs');
const https = require('https');
const path = require('path');

const images = [
  { name: 'Kanchipuram Silk Saree', url: 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=600&q=80' },
  { name: 'Banarasi Zari Saree', url: 'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?w=600&q=80' },
  { name: 'Premium Cotton Saree', url: 'https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=600&q=80' },
  { name: 'Handloom Cotton Shirt', url: 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=600&q=80' },
  { name: 'Pure Silk Dhoti Set', url: 'https://images.unsplash.com/photo-1611601679655-7c8bc197f0c6?w=600&q=80' },
  { name: 'Wedding Silk Kurta', url: 'https://images.unsplash.com/photo-1597113366853-9a93ad3f1002?w=600&q=80' },
  { name: 'Chanderi Suit Material', url: 'https://images.unsplash.com/photo-1593030761757-71fae45fa0e7?w=600&q=80' },
  { name: 'Embroidered Fabric Set', url: 'https://images.unsplash.com/photo-1589310243389-96a5483213a8?w=600&q=80' },
  { name: 'Cotton Bedspread Set', url: 'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=600&q=80' },
  { name: 'Egyptian Cotton Towels', url: 'https://images.unsplash.com/photo-1560064060-1f0124976cae?w=600&q=80' },
  { name: 'Mysore Silk Special', url: 'https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=600&q=80' },
  { name: 'Pashmina Winter Shawl', url: 'https://images.unsplash.com/photo-1520903920243-00d872a2d1c9?w=600&q=80' },
  { name: "Mens Wedding Sherwani", url: 'https://images.unsplash.com/photo-1623091410901-00e2d268901f?w=600&q=80' },
  { name: 'Chettinad Cotton Saree', url: 'https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=600&q=80' },
  { name: 'Designer Anarkali Suit', url: 'https://images.unsplash.com/photo-1584483733075-8bd3624dfdf2?w=600&q=80' },
  { name: 'Velvet Bedspread', url: 'https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=600&q=80' },
];

const dir = path.join(__dirname, 'public', 'images');
if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

async function download(url, dest) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        return resolve(download(res.headers.location, dest));
      }
      const file = fs.createWriteStream(dest);
      res.pipe(file);
      file.on('finish', () => {
        file.close();
        resolve();
      });
    }).on('error', (err) => {
      fs.unlink(dest, () => {});
      reject(err);
    });
  });
}

async function run() {
  for (const img of images) {
    const p = path.join(dir, `${img.name}.jpg`);
    await download(img.url, p);
    console.log(`Downloaded ${img.name}.jpg`);
  }
}

run();
