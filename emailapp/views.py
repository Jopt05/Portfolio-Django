from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status
from decouple import config
from smtplib import SMTPException

from .serializers import SendEmailSerializer

# Create your views here.

from_email = config("FROM_EMAIL")
to_email = config("TO_EMAIL")


class EmailView(APIView):

    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)
        error_message = ''

        if (serializer.is_valid()):
            name = serializer.validated_data["name"]
            email = serializer.validated_data["email"]
            message = serializer.validated_data["message"]

            try:

                was_sended = send_mail(
                    subject=f"New mail from {name} - {email}",
                    message=message,
                    from_email=from_email,
                    recipient_list=[to_email],
                    fail_silently=False,
                )

            except SMTPException as e:
                print(e)
                return Response(
                    {
                        "ok": False
                    },
                    status=status.HTTP_200_OK
                )
            except:
                print("Mail Sending Failed!")

        else:
            return Response(
                {
                    "ok": False,
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
