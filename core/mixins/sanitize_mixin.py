import bleach
from django.conf import settings


class BleachSanitizeMixin:
    def sanitize_input(self, key, value):
        # Vérifie si la clé est dans les champs exclus de Bleach
        if key in getattr(settings, 'BLEACH_EXLUDE_FIELDS', []):
            return value
        # Si la valeur est une chaîne de caractères
        if isinstance(value, str):
            # Nettoie la valeur avec Bleach
            return bleach.clean(
                value,
                tags=getattr(settings, 'BLEACH_ALLOWED_TAGS', []),
                attributes=getattr(settings, 'BLEACH_ALLOWED_ATTRIBUTES', {}),
                strip=True,
            )
        # Si la valeur est un dictionnaire
        elif isinstance(value, dict):
            # Applique récursivement la fonction à chaque élément du dictionnaire
            return {k: self.sanitize_input(k, v) for k, v in value.items()}
        # Si la valeur est une liste
        elif isinstance(value, list):
            # Applique récursivement la fonction à chaque élément de la liste
            return [self.sanitize_input(key, item) for item in value]
        # Si la valeur n'est ni une chaîne, ni un dictionnaire, ni une liste, la retourne telle quelle
        return value

    def to_internal_value(self, data):
        # Nettoie les données d'entrée avec Bleach
        cleaned_data = {}
        # Parcourt les clés et les valeurs du dictionnaire
        for key, value in data.items():
            cleaned_data[key] = self.sanitize_input(key, value)
        return super().to_internal_value(cleaned_data)
