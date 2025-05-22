import logging
from sentry_sdk import capture_exception
from rest_framework.response import Response
from rest_framework import status


logger = logging.getLogger('django')


def handle_create_view(view_instance, request, *args, **kwargs):
    try:
        logger.info(f"[REGISTER] Tentative de création : {request.data}")

        response = super(view_instance.__class__, view_instance).create(request, *args, **kwargs)

        if response.status_code < 400:
            logger.info(f"[REGISTER SUCCÈS] Instance créé : {response.data}")
        else:
            logger.warning(f"[REGISTER ÉCHEC] Code {response.status_code} - Réponse : {response.data}")

        return response

    except Exception as e:
        logger.error(f"[REGISTER ERREUR] Erreur : {str(e)}", exc_info=True)
        capture_exception(e)
        return Response(
            {"detail": "Une erreur s'est produite lors de la creation de l'instance."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
