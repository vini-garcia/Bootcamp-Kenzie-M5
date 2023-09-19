from rest_framework.views import APIView, Request, Response, status
from django.forms import model_to_dict
from teams.models import Team
from utils import data_processing
from exceptions import (
    ImpossibleTitlesError,
    InvalidYearCupError,
    NegativeTitlesError,
)


class TeamView(APIView):
    def get(self, request: Request) -> Response:
        soccer_teams = Team.objects.all()
        soccer_teams_dict = []

        for team in soccer_teams:
            current_team = model_to_dict(team)
            soccer_teams_dict.append(current_team)

        return Response(soccer_teams_dict, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        try:
            data_processing(request.data)

            team = Team.objects.create(**request.data)
            converted_team = model_to_dict(team)

            return Response(converted_team, status.HTTP_201_CREATED)
        except (
            NegativeTitlesError,
            InvalidYearCupError,
            ImpossibleTitlesError,
        ) as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        converted_team = model_to_dict(team)
        return Response(converted_team, status.HTTP_200_OK)

    def patch(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)
        team.id = team_id
        team.save()

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
