# Webeazzy - AI-Powered Solutions for Modern Web

A beautiful, modern static website for Webeazzy's AI-powered services, featuring a darker theme inspired by HeroUI.

## 🚀 Features

### Main Landing Page (`index.html`)
- Modern, responsive design with dark theme
- Showcase of Webeazzy services (BG Remover & AI Website Builder)
- Smooth animations and hover effects
- Interactive service cards
- Professional footer with links

### BG Removal Service Page (`bgremove.html`)
- Interactive demo section with drag-and-drop file upload
- Comprehensive pricing page with 4 tiers:
  - **Starter**: $0.02/image (₹1.40 per image)
  - **Basic Package**: $15 for 1,000 images (Save 25%)
  - **Pro Package**: $50 for 5,000 images (Save 50%) - Most Popular
  - **Enterprise**: $200 for 25,000 images (Save 60%)
- API documentation section
- Feature highlights
- Beautiful gradient effects and animations

## 🎨 Design Features

- **HeroUI-Inspired Theme**: Modern dark theme with blue (#0072f5) and purple (#7828c8) gradients
- **Responsive**: Mobile-first design that works on all devices
- **Animations**: Floating elements, fade-ins, and smooth transitions
- **Interactive Elements**: Hover effects, card animations, and smooth scrolling
- **Modern UI**: Clean, professional design with attention to detail

## 📁 Project Structure

```
webeazzy_static/
├── index.html          # Main landing page
├── bgremove.html       # BG removal service page with pricing
└── README.md           # This file
```

## 🛠️ Technologies Used

- **HTML5**: Semantic markup
- **Tailwind CSS**: Utility-first CSS framework (via CDN)
- **Font Awesome**: Icon library
- **Google Fonts**: Inter font family
- **Vanilla JavaScript**: Interactive functionality

## 🚀 Getting Started

### Option 1: Open Directly
Simply open `index.html` or `bgremove.html` in your web browser.

### Option 2: Use a Local Server

Using Python:
```bash
python3 -m http.server 8000
```

Using Node.js (npx):
```bash
npx serve .
```

Using PHP:
```bash
php -S localhost:8000
```

Then visit:
- Main page: `http://localhost:8000/index.html`
- BG Remover: `http://localhost:8000/bgremove.html`

## 💰 Pricing Details

All prices are based on ₹1.40 per image (approximately $0.017), converted to USD:

| Package | Images | Price | Per Image | Savings |
|---------|--------|-------|-----------|---------|
| Starter | Pay as you go | $0.02 | $0.02 | - |
| Basic | 1,000 | $15 | $0.015 | 25% |
| Pro | 5,000 | $100 | $0.02 | Best Value |
| Enterprise | Unlimited | Custom | Contact Us | Tailored |

## 🎯 Key Features

### BG Removal Service
- AI-powered with 99.9% accuracy
- Process images in under 3 seconds
- High-resolution support (up to 25MP)
- Transparent PNG output
- Batch processing
- RESTful API
- Multiple SDK support (Python, JavaScript, PHP, Java)

### Main Website
- Service showcase
- Feature highlights
- Modern animations
- Professional branding
- Easy navigation

## 🎨 Color Scheme

- **Primary Blue**: `#0072f5`
- **Secondary Purple**: `#7828c8`
- **Background**: `#000000` (Black)
- **Card Background**: `#18181b`
- **Border**: `#27272a`

## 📱 Responsive Design

The website is fully responsive and optimized for:
- Desktop (1920px+)
- Laptop (1280px - 1920px)
- Tablet (768px - 1280px)
- Mobile (320px - 768px)

## 🔧 Customization

### Change Colors
Edit the Tailwind config in the `<script>` tag:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: '#0072f5',    // Change primary color
                secondary: '#7828c8',  // Change secondary color
            }
        }
    }
}
```

### Update Pricing
Edit the pricing cards in `bgremove.html` to update prices, features, or packages.

### Add Content
Simply edit the HTML files to add or modify content, sections, or features.

## 🌐 Domain Setup

This is designed for:
- Main site: `webeazzy.com`
- BG Remover: `bgremove.webeazzy.com`

## 📄 License

© 2025 Webeazzy. All rights reserved.

## 🤝 Support

For questions or support, contact the Webeazzy team.

---

**Built with ❤️ for Webeazzy**

# webeazzy-static
