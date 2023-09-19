from rest_framework.views import Request, Response, status, APIView
from .models import Pet
from groups.models import Group
from traits.models import Trait
from .serializers import PetSerializer
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


class PetsView(APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        trait = request.query_params.get("trait")

        if trait:
            pets = Pet.objects.filter(traits__name__iexact=trait)

        else:
            pets = Pet.objects.all()

        result = self.paginate_queryset(pets, request)
        serializer = PetSerializer(result, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        group_data = serializer.validated_data.pop("group", None)
        traits_data = serializer.validated_data.pop("traits", None)

        if group_data:
            try:
                checked_group = Group.objects.get(
                    scientific_name__iexact=group_data["scientific_name"]
                )
            except Group.DoesNotExist:
                checked_group = Group.objects.create(**request.data["group"])

        pet = Pet.objects.create(
            **serializer.validated_data, group=checked_group)

        if traits_data:
            for trait in traits_data:
                try:
                    new_trait = Trait.objects.get(name__iexact=trait["name"])
                except Trait.DoesNotExist:
                    new_trait = Trait.objects.create(**trait)

                pet.traits.add(new_trait)

        serializer = PetSerializer(pet)
        return Response(serializer.data, status.HTTP_201_CREATED)


class PetDetailView(APIView):
    def get(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        group_data = serializer.validated_data.pop("group", None)
        traits_data = serializer.validated_data.pop("traits", None)

        if group_data:
            try:
                checked_group = Group.objects.get(
                    scientific_name__iexact=group_data["scientific_name"]
                )
            except Group.DoesNotExist:
                checked_group = Group.objects.create(**request.data["group"])
            pet.group = checked_group

        if traits_data:
            pet.traits.clear()
            for trait in traits_data:
                try:
                    new_trait = Trait.objects.get(name__iexact=trait["name"])
                except Trait.DoesNotExist:
                    new_trait = Trait.objects.create(**trait)
                pet.traits.add(new_trait)

        for key, value in serializer.validated_data.items():
            setattr(pet, key, value)

        pet.save()
        serializer = PetSerializer(pet)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
