from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework import status

class ListMixinAPI:
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateMiximAPI:
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveMiximAPI:
    def retrieve(self, request, *args, **kwargs):
        #messages = self.get_object(kwargs['pk'])
        serializer = self.serializer_class(instance=self.get_object(kwargs['pk']))
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateMiximAPI:
    def update(self, request, *args, **kwargs):
        #messages = self.get_object(kwargs['pk'])
        serializer = self.serializer_class(instance=self.get_object(kwargs['pk']), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(kwargs['pk']), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteMiximAPI:
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object(kwargs['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MyAPIView(views.APIView):
    serializer_class = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()

    def get_object(self, pk):
        return generics.get_object_or_404(self.model, pk=pk)


