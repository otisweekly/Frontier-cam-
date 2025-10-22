# 🚀 Deployment Guide - Access on iPhone

The camera app requires HTTPS to access the camera (except on localhost). Here are your deployment options:

---

## ⚡ Quick Deploy (5 minutes)

### Option 1: Netlify (Easiest - Drag & Drop)

1. Go to [netlify.com](https://netlify.com) and sign up (free)
2. Click "Add new site" → "Deploy manually"
3. Drag and drop the `index.html` file
4. Get your URL: `https://your-app.netlify.app`
5. Open URL on your iPhone Safari ✅

**Pros**: Instant, no config, free HTTPS
**Cons**: Random URL (can customize with paid plan)

---

### Option 2: GitHub Pages

1. **Enable GitHub Pages**:
   - Go to your repo on GitHub
   - Settings → Pages
   - Source: Deploy from branch
   - Branch: `claude/leica-rangefinder-camera-app-011CUNkcc8NxJWZpyP8oZ1KN`
   - Folder: `/ (root)`
   - Save

2. **Access your app**:
   - URL will be: `https://yourusername.github.io/Frontier-cam-/`
   - Wait 2-3 minutes for deployment
   - Open on iPhone Safari ✅

**Pros**: Free, tied to your repo
**Cons**: Public URL (unless private repo)

---

### Option 3: Vercel (Fast Deploy)

1. Go to [vercel.com](https://vercel.com) and sign up (free)
2. Click "Add New" → "Project"
3. Import your GitHub repo
4. Deploy (automatic)
5. Get URL: `https://your-app.vercel.app`
6. Open on iPhone ✅

**Pros**: Fast, auto-deploys on push, free HTTPS
**Cons**: Requires GitHub connection

---

## 🏠 Local Testing (Same WiFi Network)

If you want to test locally before deploying:

### Using Python (Mac/Linux)

```bash
# In the Frontier-cam- directory:
python3 -m http.server 8000
```

Then on your iPhone (connected to same WiFi):
1. Find your computer's IP address:
   - Mac: System Preferences → Network
   - Linux: `ifconfig` or `ip addr`
2. Open Safari: `http://YOUR-IP:8000`

**⚠️ Note**: Camera might not work over HTTP (non-HTTPS). Use HTTPS deployments above for full functionality.

---

## 🔒 Why You Need a Server

The camera app won't work by opening `index.html` directly because:

1. **Camera API requires HTTPS** (or localhost)
2. **File:// protocol** doesn't support getUserMedia()
3. **Same-origin policy** restrictions

---

## ✅ Recommended for iPhone

**Best option**: Netlify (fastest, easiest)
**Best for development**: GitHub Pages (integrated with repo)
**Best for production**: Vercel (auto-deploys)

---

## 📱 Accessing on iPhone

Once deployed:

1. Open Safari (not Chrome - better camera support)
2. Navigate to your deployed URL
3. Tap "Enable Camera"
4. Grant camera permissions
5. Start shooting! 📷

For best experience, add to home screen:
- Tap share icon → "Add to Home Screen"
- App will open fullscreen like a native app

---

## 🆘 Troubleshooting

**"Camera access denied"**
- Check iPhone Settings → Safari → Camera: Allow

**"Not loading"**
- Wait 2-3 minutes after deploying (GitHub Pages)
- Check HTTPS (not HTTP)
- Clear Safari cache

**"Black screen"**
- Ensure good lighting
- Try different camera (front/back)
- Restart Safari

---

## 🎯 Quick Start Command

If you just want to test locally RIGHT NOW:

```bash
cd /home/user/Frontier-cam-
python3 -m http.server 8000
```

Then visit: `http://localhost:8000` on your computer

(Note: Won't work on iPhone without ngrok/tunneling due to different device)

---

Need help? Check the deployment platform's docs:
- [Netlify Docs](https://docs.netlify.com)
- [GitHub Pages Docs](https://docs.github.com/pages)
- [Vercel Docs](https://vercel.com/docs)
