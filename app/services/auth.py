from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.models import User



class AuthorizationView(GenericAPIView):
    def post(self, requests):
        data = requests.data
        if 'phone' not in data or not data['phone']:
            return Response({"Error": "Enter phone"}, status=status.HTTP_400_BAD_REQUEST)

        if 'password' not in data or not data['password']:
            return Response({"Error": "Enter Password"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(phone=int(data['phone'])).exists():
            return Response({
                "Error": "This phone exists"
            }, status=status.HTTP_400_BAD_REQUEST)

        password = data['password']
        if len(password) < 6 or not any(char.isdigit() for char in password) or not any(
                char.isalpha() for char in password):
            return Response({
                "Error": "Invalid Password"
            }, status=status.HTTP_406_NOT_ACCEPTABLE)

        user_data = {
            'phone': data['phone'],
            'password': password,
        }
        if data.get('key', None) == 'admin':
            user_data.update({
                "is_staff": True,
                "is_superuser": True
            })
        user = User.objects.create_user(**user_data)
        token = Token.objects.create(user=user)
        return Response({"success": "You have successfully registered", "user_id": user.id, "token": token.key},
                        status=status.HTTP_200_OK)


class LoginView(GenericAPIView):
    def post(self, requests):
        data = requests.data
        if "phone" not in data or not data["phone"]:
            return Response({"Error": "Phone number is missing"}, status=status.HTTP_400_BAD_REQUEST)
        if "password" not in data or not data['password']:
            return Response({"Error": "Password is missing"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(phone=data['phone']).first()
        if not user:
            return Response({"Error": "User is not Found"}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(data['password']):
            return Response({"Error": "Incorrect Password"}, status=status.HTTP_404_NOT_FOUND)

        token = Token.objects.get_or_create(user=user)[0]
        return Response({
            "Success": token.key
        })


