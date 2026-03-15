# Rayan ALPHA — Advanced E-Commerce Platform

A production-ready, full-stack premium textile e-commerce platform built with **Next.js 16**, **TypeScript**, and **Tailwind CSS**.

## 🌐 Live Demo
> Deployed at: *(Vercel URL goes here after deployment)*

## ✨ Features
- 🛒 Full shopping cart with persistent state (Zustand)
- 💎 16 Premium textile products with Tamil localization
- 🔍 Real-time search, sort, and category filtering
- 💳 Secure multi-step checkout system
- 🧾 Order management with live database
- 👤 User authentication (Admin + Customer roles)
- 📊 Admin dashboard with revenue analytics & inventory tracking
- ❤️ Wishlist system
- 📱 Fully responsive mobile-first design
- 🎨 Premium UI/UX (Apple + Amazon inspired)

## 🚀 Tech Stack
| Layer | Technology |
|-------|-----------|
| Framework | Next.js 16 (App Router) |
| Language | TypeScript |
| Styling | Tailwind CSS v4 |
| State | Zustand |
| Database | JSON File (Local) / Vercel KV (Production) |
| Font | Inter (Google Fonts) |

## 📂 Project Structure
```
src/
├── app/
│   ├── page.tsx           # Homepage with hero slider
│   ├── products/          # Product listing with filters
│   ├── product/[id]/      # Product detail page
│   ├── cart/              # Shopping cart
│   ├── checkout/          # Checkout + payment
│   ├── login/             # Auth page
│   ├── admin/             # Admin dashboard
│   ├── order-success/     # Order confirmation
│   └── api/               # REST API routes
│       ├── products/
│       ├── orders/
│       └── auth/login/
├── components/
│   └── Navbar.tsx         # Navigation
└── lib/
    ├── db.ts              # Database layer
    └── store.ts           # Zustand global state
```

## 🛠️ Local Development

1. **Install dependencies:**
   ```bash
   npm install
   ```
2. **Run development server:**
   ```bash
   npm run dev
   ```
3. **Open browser:** http://localhost:3000

## 🔑 Demo Credentials
| Role | Email | Password |
|------|-------|----------|
| Admin | admin@rayana.com | password |
| Customer | user@rayana.com | password |

## 🚢 Deploy to Vercel (Free)
1. Push this repo to GitHub
2. Go to [vercel.com](https://vercel.com) → **Import Project**
3. Select this GitHub repository
4. Click **Deploy** — done in 60 seconds!

---

&copy; 2026 Rayan ALPHA Enterprise. Built with ❤️ using Next.js + Tailwind CSS.
