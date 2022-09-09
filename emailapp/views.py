from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status
from decouple import config

from .serializers import SendEmailSerializer

# Create your views here.

from_email = config("FROM_EMAIL")
to_email = config("TO_EMAIL")


class EmailView(APIView):

    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)

        if (serializer.is_valid()):
            name = serializer.validated_data["name"]
            email = serializer.validated_data["email"]
            message = serializer.validated_data["message"]

            was_sended = send_mail(
                subject=f"New mail from {name} - {email}",
                message=message,
                from_email=from_email,
                recipient_list=[to_email],
                fail_silently=False,
            )

            if was_sended:
                return Response(
                    {
                        "ok": True
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "ok": False,
                        "message": str(e)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        else:
            return Response(
                {
                    "ok": False,
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
