# SP500 Film Simulator - Deployment Guide

Quick guide to deploy the SP500 Film Simulator PWA to production.

## 📋 Pre-Deployment Checklist

Before deploying, make sure you have:

- [ ] Generated app icons (run `generate-icons.html` in browser)
- [ ] Downloaded all three icons (180px, 192px, 512px)
- [ ] Placed icons in project root directory
- [ ] Tested locally on iPhone (if possible)
- [ ] Updated manifest.json with your domain
- [ ] Updated service worker cache name if needed

## 🚀 Quick Deploy (Netlify - Recommended)

### Option 1: Drag & Drop (Easiest)

1. **Generate Icons First**:
   ```bash
   open generate-icons.html
   # Click download for all 3 icons
   # Save to project root
   ```

2. **Deploy to Netlify**:
   - Visit [netlify.com](https://netlify.com)
   - Sign in (or create free account)
   - Drag project folder onto deploy area
   - Wait for deployment to complete
   - Your site is live! 🎉

3. **Custom Domain (Optional)**:
   - Go to Site Settings → Domain Management
   - Add custom domain (e.g., `sp500.yourdomain.com`)
   - Configure DNS as instructed

### Option 2: Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
netlify deploy --prod
# Follow prompts, choose project directory

# Your site is now live!
```

### Option 3: Git-based Deploy

```bash
# Connect to GitHub repo
# In Netlify dashboard:
# - New site from Git
# - Connect to GitHub
# - Select repository
# - Build settings: None needed (static site)
# - Deploy!

# Auto-deploys on every git push
```

## 🔧 Alternative Platforms

### Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod

# Follow prompts
# Your site is live!
```

### GitHub Pages

```bash
# 1. Push to GitHub
git add .
git commit -m "Add SP500 Film Simulator"
git push origin main

# 2. Enable GitHub Pages
# Go to repo Settings → Pages
# Source: Deploy from branch
# Branch: main
# Folder: / (root)
# Save

# 3. Access your site
# https://yourusername.github.io/repo-name/sp500.html
```

### Cloudflare Pages

1. Go to [Cloudflare Pages](https://pages.cloudflare.com)
2. Create new project
3. Connect to Git repository
4. Deploy (auto-builds on push)

## 📱 iOS PWA Setup

### After Deployment

1. **Test on iPhone**:
   ```
   Open Safari → Navigate to your deployed URL
   ```

2. **Add to Home Screen**:
   - Tap Share button (⎋)
   - Scroll down → "Add to Home Screen"
   - Tap "Add"
   - App appears on home screen! 📱

3. **Test Offline**:
   - Open app from home screen
   - Turn on airplane mode
   - App should still load (service worker cached)

## 🔍 Testing Checklist

After deployment, test these features:

### Core Functionality
- [ ] Upload 1 photo successfully
- [ ] Upload multiple photos (up to 36)
- [ ] Thumbnail filmstrip displays correctly
- [ ] Swipe left/right navigation works
- [ ] Before/after toggle works
- [ ] All controls update preview in real-time

### Image Processing
- [ ] Tone adjustments produce visible changes
- [ ] CMY color correction works correctly
- [ ] Density slider affects brightness
- [ ] Hypertone modes show differences
- [ ] Film grain applies correctly
- [ ] Sharpness levels work
- [ ] Saturation slider works

### Batch Operations
- [ ] "Copy to All" applies settings to all photos
- [ ] "Process All" processes all photos
- [ ] "Reset" resets current photo settings

### Export
- [ ] Single photo export triggers share sheet (iOS)
- [ ] Multiple photo export downloads files
- [ ] Exported photos have correct quality
- [ ] File naming is correct (sp500_frame_001.jpg)

### PWA Features
- [ ] Installs as PWA (Add to Home Screen)
- [ ] Runs in standalone mode (no browser chrome)
- [ ] Service worker caches correctly
- [ ] Works offline after first load
- [ ] Safe area insets respect notch/home indicator

### iOS Optimizations
- [ ] Haptic feedback works on supported devices
- [ ] No zoom on input focus
- [ ] Smooth scrolling on filmstrip
- [ ] Dark theme displays correctly
- [ ] Large touch targets easy to tap

## 🐛 Common Issues

### Icons Not Showing

**Problem**: App icon is blank or shows browser default

**Solution**:
```bash
# Make sure you generated and uploaded all icons:
# - icon-180.png
# - icon-192.png
# - icon-512.png

# Check manifest.json paths match
# Re-add to home screen after fixing
```

### Service Worker Not Updating

**Problem**: App doesn't reflect latest changes

**Solution**:
```javascript
// Update cache name in sw.js:
const CACHE_NAME = 'sp500-v2'; // Increment version

// Or clear cache in browser:
// Safari → Settings → Clear History and Website Data
```

### HEIC Upload Fails

**Problem**: iPhone HEIC photos won't upload

**Note**: HEIC support requires external library (`heic2any`)

**Temporary solution**:
- Change iPhone settings: Settings → Camera → Formats → Most Compatible
- This makes iPhone shoot JPG instead of HEIC

**Long-term solution**:
```html
<!-- Add heic2any library to sp500.html -->
<script src="https://cdn.jsdelivr.net/npm/heic2any@0.0.4/dist/heic2any.min.js"></script>
```

### Export Downloads Instead of Share Sheet (iOS)

**Problem**: Export button downloads instead of showing share sheet

**Cause**: Web Share API only works on HTTPS

**Solution**:
- Ensure site is served over HTTPS (Netlify/Vercel do this automatically)
- Test in Safari (not Chrome on iOS)

## 📊 Analytics (Optional)

Add analytics to track usage:

```html
<!-- Add before </head> in sp500.html -->

<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>

<!-- Or Plausible (privacy-friendly) -->
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/script.js"></script>
```

## 🔐 Security Headers

Already configured in `netlify.toml`:

```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "no-referrer"
    Permissions-Policy = "camera=(), microphone=()"
```

## 🌍 Custom Domain Setup

### Netlify

1. **Purchase domain** (Namecheap, Google Domains, etc.)

2. **Add to Netlify**:
   ```
   Site Settings → Domain Management → Add custom domain
   ```

3. **Configure DNS**:
   ```
   # Add CNAME record:
   sp500.yourdomain.com → your-site.netlify.app
   ```

4. **Enable HTTPS**:
   - Automatic with Netlify (Let's Encrypt)
   - Wait ~1 hour for certificate

### Recommended Domains

- `sp500.yourdomain.com` - Professional
- `app.sp500.com` - Clean, app-focused
- `scan.sp500.com` - Scanner theme
- `lab.sp500.com` - Photo lab theme

## 📈 Performance Optimization

### Image Processing Performance

Current implementation processes images on main thread. For better performance:

```javascript
// TODO: Implement Web Worker
// Create processWorker.js:
self.addEventListener('message', (e) => {
  const { imageData, settings } = e.data;
  const processed = processImage(imageData, settings);
  self.postMessage({ processed });
});

// Use in main app:
const worker = new Worker('processWorker.js');
worker.postMessage({ imageData, settings });
worker.onmessage = (e) => {
  renderPreview(e.data.processed);
};
```

### Caching Strategy

Current strategy: Cache-first with network fallback

To update strategy, edit `sw.js`:

```javascript
// Network-first (always get latest):
event.respondWith(
  fetch(event.request)
    .catch(() => caches.match(event.request))
);

// Stale-while-revalidate (fast + fresh):
event.respondWith(
  caches.match(event.request)
    .then(cached => {
      const fetched = fetch(event.request)
        .then(response => {
          caches.open(CACHE_NAME)
            .then(cache => cache.put(event.request, response));
          return response.clone();
        });
      return cached || fetched;
    })
);
```

## 🎯 Next Steps

After successful deployment:

1. **Share with beta testers** (friends, photography community)
2. **Gather feedback** on image processing quality
3. **Iterate on processing algorithms** based on feedback
4. **Add more features** from V2 roadmap
5. **Consider native iOS app** if successful

## 📞 Support

If you encounter issues:

1. Check browser console for errors
2. Test in latest Safari/Chrome
3. Clear cache and try again
4. Open GitHub issue with details

---

**Congratulations!** 🎉

Your SP500 Film Simulator is now live and accessible from any iPhone!

Share your URL with the world and start transforming digital photos into beautiful film scans.
