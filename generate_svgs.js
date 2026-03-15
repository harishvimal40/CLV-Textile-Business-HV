const fs = require('fs');
const path = require('path');

const images = [
  { name: 'Kanchipuram Silk Saree', color: '#4f46e5' },
  { name: 'Banarasi Zari Saree', color: '#ec4899' },
  { name: 'Premium Cotton Saree', color: '#0ea5e9' },
  { name: 'Handloom Cotton Shirt', color: '#f59e0b' },
  { name: 'Pure Silk Dhoti Set', color: '#8b5cf6' },
  { name: 'Wedding Silk Kurta', color: '#10b981' },
  { name: 'Chanderi Suit Material', color: '#f43f5e' },
  { name: 'Embroidered Fabric Set', color: '#6366f1' },
  { name: 'Cotton Bedspread Set', color: '#14b8a6' },
  { name: 'Egyptian Cotton Towels', color: '#06b6d4' },
  { name: 'Mysore Silk Special', color: '#d946ef' },
  { name: 'Pashmina Winter Shawl', color: '#eab308' },
  { name: "Mens Wedding Sherwani", color: '#64748b' },
  { name: 'Chettinad Cotton Saree', color: '#ef4444' },
  { name: 'Designer Anarkali Suit', color: '#84cc16' },
  { name: 'Velvet Bedspread', color: '#0f766e' },
];

const dir = path.join(__dirname, 'public', 'images');
if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

for (const img of images) {
  const svgContent = `
<svg width="600" height="600" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="600" fill="${img.color}"/>
  <text x="50%" y="50%" font-family="system-ui, -apple-system, sans-serif" font-size="32" font-weight="900" fill="white" dominant-baseline="middle" text-anchor="middle">
    ${img.name}
  </text>
  <text x="50%" y="58%" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="normal" fill="rgba(255,255,255,0.7)" dominant-baseline="middle" text-anchor="middle">
    RAYAN STORES
  </text>
</svg>
  `.trim();

  const p = path.join(dir, `${img.name.replace(/\s+/g, '_')}.svg`);
  fs.writeFileSync(p, svgContent);
  console.log(`Generated: ${p}`);
}
