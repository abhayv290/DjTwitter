#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r req.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

if [[ $CREATE_SUPERUSER ]]
then 
    python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="$SUPERUSER_USERNAME").exists():
    User.objects.create_superuser(
        username="$SUPERUSER_USERNAME",
        email="$SUPERUSER_EMAIL",
        password="$SUPERUSER_PASSWORD"
    )
EOF
fi
