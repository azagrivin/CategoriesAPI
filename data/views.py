from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from data.models import Category as ModelCategory


class Categories(APIView):
    def post(self, request):
        self.create(request.data)
        return Response(status=status.HTTP_201_CREATED)

    @staticmethod
    def create(data, parents=None):
        category = ModelCategory.objects.create(name=data['name'])
        category.save()

        try:
            for children in data['children']:
                child = Categories.create(children, parents)
                category.childrens.add(child)
        except KeyError:
            # not find children
            pass

        return category


class Category(APIView):
    def get(self, request, id):
        category = get_object_or_404(ModelCategory, id=id)
        response = {
            'id': category.id,
            'name': category.name,
            'children': self.children(category)
        }

        parents = []
        firstParent = parent = category.category_set.first()
        while parent:
            parents.append({'id': parent.id, 'name': parent.name})
            parent = parent.category_set.first()
        response['parents'] = parents

        try:
            response['siblings'] = [{'id': sibling.id, 'name': sibling.name} for sibling in firstParent.childrens.all()
                                    if sibling.id != category.id]
        except AttributeError:
            response['siblings'] = []

        return Response(response, status=status.HTTP_200_OK)

    @staticmethod
    def children(category):
        childrens = []
        for children in category.childrens.all():
            childrens.append({
                'id': children.id,
                'name': children.name
            })
        return childrens
