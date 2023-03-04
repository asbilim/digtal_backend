from rest_framework.serializers import ModelSerializer
from website.models import Contact, Newsletter,Employee

class ContactSerializer(ModelSerializer):

    class Meta:
        
        model = Contact
        fields ='__all__'


class NewsletterSerializer(ModelSerializer):

    class Meta:

        model = Newsletter
        fields = '__all__'

class EmployeeSerializer(ModelSerializer):

    class Meta:
        
        model= Employee
        fields = '__all__'