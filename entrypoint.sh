#!/usr/bin/env bash
set -e

echo "🚀 Starte Django Setup..."

python manage.py migrate --noinput

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')
    print("✅ Superuser erstellt: ${DJANGO_SUPERUSER_USERNAME}")
else:
    print("ℹ️ Superuser existiert bereits")
EOF

echo "🌍 Starte Django Development Server auf Port 6060..."
exec python manage.py runserver 0.0.0.0:6060
