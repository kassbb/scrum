from sentry_sdk import capture_message


# Middleware pour enregistrer les erreurs HTTP avec Sentry
class SentryHttpErrorLoggerMiddleware:
    def __init__(self, get_response):
        # Initialisation avec la fonction de réponse
        self.get_response = get_response

    def __call__(self, request):
        # Appel de la fonction de réponse
        response = self.get_response(request)

        # Vérification si le code de statut est une erreur (400 ou plus)
        if response.status_code >= 400:
            # Capture du message d'erreur avec Sentry
            capture_message(
                f"HTTP {response.status_code} error on {request.path}",
                level="warning" if response.status_code < 500 else "error"
            )

        # Retour de la réponse
        return response
