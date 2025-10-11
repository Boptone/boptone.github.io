# Boptone - Own Your Tone

**Your personal AI manager who learns your style, knows your goals, and helps you navigate every decision in your music career.**

## 🚀 Features

- **AI-Powered Career Advice**: Get expert guidance on release strategy, marketing, business deals, and more
- **Personalized Responses**: AI learns your style and goals for increasingly tailored advice  
- **Stripe Integration**: Complete subscription system with 14-day free trials
- **User Authentication**: Secure account creation and login system
- **Conversation Memory**: AI remembers your previous interactions
- **Professional UI**: Modern, responsive design built with React and Tailwind CSS

## 🛠️ Tech Stack

- **Backend**: Python Flask with SQLite database
- **Frontend**: React with Vite and Tailwind CSS  
- **AI**: OpenAI GPT-4o-mini for music industry expertise
- **Payments**: Stripe for subscription management
- **Authentication**: JWT tokens for secure sessions

## 🔧 Environment Variables

Create a `.env` file or set these environment variables:

```
OPENAI_API_KEY=your_openai_api_key_here
FLASK_SECRET_KEY=your_secret_key_here
FLASK_ENV=production
```

## 🚀 Quick Deploy to Railway

1. Fork this repository
2. Connect to Railway at railway.app
3. Add environment variables in Railway dashboard
4. Deploy automatically!

## 💡 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Run the server
python run_server.py
```

## 📊 API Endpoints

- `GET /` - Main website
- `POST /api/ai/demo-response` - AI chat for demos
- `POST /api/ai/chat` - Full AI chat with memory
- `POST /api/auth/signup` - User registration
- `POST /api/auth/signin` - User login
- `POST /api/stripe/create-checkout-session` - Stripe payments

## 🎯 Mission

Boptone is building the world's first autonomous operating system for independent artists. We're starting with AI-powered career advice and expanding toward a complete artist platform including healthcare, funding, distribution, and more.

## 📄 License

MIT License - Build amazing things for artists!

---

**Ready to revolutionize the music industry? Deploy Boptone and help artists truly own their tone! 🎵**
