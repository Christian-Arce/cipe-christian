#/bin/bash
cp -v cipe/settings.py.sample cipe/settings.py
cp -v .env.dev.sample .env.dev
echo ""
echo "This is a randomly generated secret key to put in your new .env.prod"
KEY=$(python3 -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))')
echo "SECRET_KEY=$KEY"
echo ""
echo "Remember to customize your passwords and Google Maps API KEY"

