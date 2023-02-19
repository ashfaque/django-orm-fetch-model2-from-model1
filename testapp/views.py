from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import *
from django.db.models import F, Q, Sum, fields, ExpressionWrapper, Value, Case, When, Subquery, OuterRef, FloatField, DecimalField, Count
from rest_framework.response import Response


class Test(APIView):
    permission_classes = [AllowAny]
    queryset = Model1.objects.all()

    def get(self, request, *args, **kwargs):
        m1_obj = Model1.objects.filter(is_deleted=True, id = 1).first()    # if id is given other filter is not required, but to demonstrate the filter, I've added is_deleted = True.
        m2_data = m1_obj.model2_rn.filter().values()
        # m2_data = m1_obj.model2_rn.all()
        print('m2_data using m1_obj -----> ', m2_data)
        
        
        return Response(data={
            'm2_data_using_m1_obj': list(m2_data),
        }, status = 200)
