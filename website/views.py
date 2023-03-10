# from django.shortcuts import render

from email import message
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from website.models import Contact, Newsletter,Employee
from website.serializer import ContactSerializer, NewsletterSerializer,EmployeeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
import json
import smtplib
from email.message import EmailMessage
from .tests import send_email

# variables

EMAIL_HOLDER = 'bilimdepaullilian@gmail.com'
PASSWORD_HOLDER = 'gjrjkwphzhgzouzp'
# PASSWORD_SENDER = 'nihabgkvdasfbgom'
PASSWORD_SENDER = 'Anepaspirater123@'
EMAIL_SENDER = 'contact@digtal.org'

# variables


def sendmail(subject, first_name, last_name, message, address):

    with smtplib.SMTP_SSL('smtp.ionos.de',587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_SENDER, PASSWORD_SENDER)
        variable_message = f' \n send by {first_name} {last_name}  for {subject} with the email {address} '
        email = EmailMessage()
        email['to'] = EMAIL_HOLDER
        email['from'] = EMAIL_SENDER
        email['subject'] = subject
        message += variable_message
        email.set_content(message)
        smtp.send_message(email)


class ContactViewSet(ModelViewSet):

    serializer_class = ContactSerializer

    def get_queryset(self):

        return Contact.objects.all()

    def create(self, request):

        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = request.data
            email = contact['email']
            first_name = contact['first_name']
            last_name = contact['last_name']
            message = contact['message']
            subject = contact['subject']
            company= contact['company_name']
            phone=contact['phone_number']
            send_email(company_name=company,interest=subject,customer_name=first_name+" "+last_name,email=email,message=message,phone_number=phone)
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]


class NewsletterViewset(ModelViewSet):

    serializer_class = NewsletterSerializer

    def get_queryset(self):
        return Newsletter.objects.all()

    def create(self, request):

        serializer = NewsletterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK, )

    def get_permissions(self):

        if self.action == "create":
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]

        return [permission() for permission in permission_classes]


class EmployeeViewset(ReadOnlyModelViewSet):

    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()

