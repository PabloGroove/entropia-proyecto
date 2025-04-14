# Entropy Password Generator 🔐

A secure password generator powered by **natural entropy** from atmospheric noise using the Random.org API.

This project leverages natural randomness to generate highly secure passwords and demonstrates a real-world application of cybersecurity and cryptography principles.

## Features

- ✅ Password generation using atmospheric noise entropy.
- ✅ API secured with personal API Key.
- ✅ Random.org integration for true randomness.
- ✅ Ready for deployment on Replit or any cloud environment.
- ✅ Configurable password length.

## Live Demo

👉 (Your live URL from Replit goes here — replace this link)

## How to Use

### Requirements

- Python 3.11+
- Random.org API key
- API Key for internal API protection

### Setup

1. Clone the repository:


git clone https://github.com/PabloGroove/entropia-proyecto.git cd entropia-proyecto


2. Install dependencies:

pip install -r requirements.txt


3. Set environment variables:
   - `SECRET_API_KEY`: Your internal API protection key.
   - `RANDOM_ORG_API_KEY`: Your Random.org API key.

You can set these variables in your environment or use tools like `.env` files.

4. Run the API locally:

uvicorn entropia_api:app --host=0.0.0.0 --port=8080


5. Access the API:

- Test root endpoint:
  `http://localhost:8080/`

- Generate password:
  `http://localhost:8080/generate-password?length=16&api_key=YOUR_SECRET_API_KEY`

## Future Improvements

- 🌍 Deploy on better public cloud (Fly.io, Render, or Vercel).
- 🌟 Add frontend interface for easier usage.
- 🔒 Rate limiting and logging.
- 💡 Add encryption for stored passwords.

## License

MIT License — feel free to use and improve!

## Author

Pablo Rivera  
Cybersecurity enthusiast & Python developer
