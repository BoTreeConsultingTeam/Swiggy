from django.shortcuts import render,redirect
from django.views import View,generic
from .models import *
from dishes.models import *
from users.models import *
from restaurant.models import *
from cart_and_orders.models import *
from django.db.models import Q
from django.views.generic import CreateView,UpdateView,DetailView,ListView,TemplateView
import json,datetime
from datetime import *
from django.http import JsonResponse
from django.contrib.auth.mixins import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.db.models.functions import TruncMonth,TruncDay
from django.db.models import Count
from cart_and_orders.cart_and_orders_serializers import *
import calendar
from collections import OrderedDict
from swiggyproject.utils import *

class MyOrdersView(View):
	def get(self,request):
		orderobject=Orders.objects.filter(user_id=request.user.id)
		print(orderobject[0].orderdate)
		return render(request,'cart_and_orders/myorders.html',{'orderobject':orderobject})

class MyOrdersDetailsView(View):
	def get(self,request):
		id=request.GET.get('id')
		orderitems=OrdersItems.objects.filter(orders_id=id)
		price=0
		for i in orderitems:
			price=price+int(i.totalprice)

		price_tax=price+(price*0.05)
		return render(request,'cart_and_orders/myorderdetails.html',{'orderitems':orderitems,'price':price,'price_tax':price_tax})

class RestaurantRecieveOrderView(View):
	def get(self,request):
		resname=Restaurant.objects.filter(user_id=request.user.id)
		print(resname[0].restaurantname)
		orderobject=Orders.objects.filter(restaurant_id=resname[0].id)
		print(orderobject)

		return render(request,'cart_and_orders/recievedorders.html',{'resname':resname,'orderobject':orderobject})

def changerestaurantorder(request):
	if request.is_ajax():
		print('hi')
		res_id=request.GET.get('restaurantid')
		resname=Restaurant.objects.filter(Q(id=res_id) & Q(user_id=request.user.id))
		orderobject=Orders.objects.filter(restaurant_id=resname[0].id)
		
		return render(request, 'cart_and_orders/changerestaurantorder.html', {'orderobject':orderobject})


class RecieveOrdersDetailsView(View):
	def get(self,request):
		id=request.GET.get('id')
		
		print(id)
		orderitems=OrdersItems.objects.filter(orders_id=id)
		print(orderitems)
		price=0
		for i in orderitems:
			price=price+int(i.totalprice)

		price_tax=price+(price*0.05)
		return render(request,'cart_and_orders/recieveorderdetails.html',{'orderitems':orderitems,'price':price,'price_tax':price_tax})	

def OrderStatusUpdate(request):
	print('status')
	orderid=request.GET.get('orderid')
	status1=request.GET.get('status1')
	order=Orders.objects.get(id=orderid)
	print('orderid=',orderid,'','status1=',status1)
	status=''
	if status1 == 'foodprepared':
		status='Food Prepared'

	elif status1 == 'orderdelivered':
		status='Order Delivered'
	else:
		status=order.orderstatus

	x=Orders.objects.filter(id=orderid).update(orderstatus=status)
	
	data={'status':status}

	print(orderid)
	print(status)
	return JsonResponse(data)

class RestaurantOrdersReports(View):
	def get(self,request):
		resname=Restaurant.objects.filter(Q(user_id=request.user.id) & Q(flag='1'))
		print(resname[0].restaurantname)
		return render(request,'cart_and_orders/restaurant_owner_report.html',{'resname':resname,'resid':resname[0].id})

#Month wise
class RestaurantOrdersReportsAPI(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None,*args,**kwargss):
		order_count_month=Orders.objects.filter(restaurant=self.kwargs['pk']).annotate(month=TruncMonth('orderdate')).values('month').annotate(total=Count('id')).order_by('month')
		print(order_count_month)
		dict1={}

		data1=OrderedDict()
		data1[1]=0
		data1[2]=0
		data1[3]=0
		data1[4]=0
		data1[5]=0
		data1[6]=0
		data1[7]=0
		data1[8]=0
		data1[9]=0
		data1[10]=0
		data1[11]=0
		data1[12]=0

		for i in order_count_month:
			#dict1[i['month'].strftime('%B')]=i['total']
			data1[i['month'].month]=i['total']
		print(data1)

		label_month,values=list(data1.keys()),list(data1.values())
		

		data={'labels':label_month,'default':values}
		return Response(data)
	# def get(self,request):
	# 	return render(request,'cart_and_orders/restaurant_owner_report.html')

#Weekly Base	
class RestaurantOrdersReportsWeeklyAPI(APIView):

	def get(self, request, format=None,*args,**kwargs):
		option=request.GET.get('option')
		print('hi',self.kwargs['pk'])
		today = datetime.now().date()
		month=today.month
		year=today.year
		start = today - timedelta(days=today.weekday())
		end = start + timedelta(days=6)
		if option=='Weekly':
			Weekly=Orders.objects.filter(orderdate__range=[start, end]).filter(restaurant_id=self.kwargs['pk']).annotate(day=TruncDay('orderdate')).values('day').annotate(total=Count('id')).order_by('day')
			print(Weekly)
			data1=OrderedDict()
			for i in range(start.day,end.day+1):
				data1[i]=0
			
			
			for i in Weekly:
				data1[i['day'].day]=i['total']
			
			weekday=[]
			for i in range(start.day,end.day+1):
				weekday.append(str(i)+'-'+str(month)+'-'+str(year))
			orders=Orders.objects.filter(orderdate__range=[start, end]).filter(restaurant_id=self.kwargs['pk']).order_by('-id')
			orderserializer=OrderSerializer(orders, many=True)
			total_list=[]
			for price in orders:
				total_list.append(float(price.totalpricetax))
			
			if total_list==[]:
				total=0
			else:
				total=sum(i for i in total_list)
			
			
			data={'labels':weekday,'default':list(data1.values()),'orderserializer':orderserializer.data,'total':total }
			return Response(data)
		elif option=='Quaterly':
			quarter1_list=[1,2,3,4]
			quarter2_list=[5,6,7,8]
			quarter3_list=[9,10,11,12]
			q1,q2,q3=0,0,0
			Quaterly=Orders.objects.filter(orderdate__year=year).filter(restaurant_id=self.kwargs['pk']).annotate(day=TruncDay('orderdate')).values('day').annotate(total=Count('id')).order_by('day')
			for i in Quaterly:
				if i['day'].month in quarter1_list:
					q1=q1+i['total']
				elif i['day'].month in quarter2_list:
					q2=q2+i['total']
				else:
					q3=q3+i['total']
			
			labels=['January-April','May-August','September-December']
			default=[q1,q2,q3]
			orders=Orders.objects.filter(orderdate__year=year).filter(restaurant_id=self.kwargs['pk']).order_by('-id')
			orderserializer=OrderSerializer(orders, many=True)
			total_list=[]
			for price in orders:
				total_list.append(float(price.totalpricetax))
			
			if total_list==[]:
				total=0
			else:
				total=sum(i for i in total_list)
			
			data={'labels':labels,'default':default,'orderserializer':orderserializer.data,'total':total }
			return Response(data)
		else:
			Monthly=Orders.objects.filter(orderdate__month=month).filter(orderdate__year=year).filter(restaurant_id=self.kwargs['pk']).annotate(day=TruncDay('orderdate')).values('day').annotate(total=Count('id')).order_by('day')
			weeks=calendar.monthcalendar(year,month)
			week1_list=weeks[0]
			week2_list=weeks[1]
			week3_list=weeks[2]
			week4_list=weeks[3]
			week5_list=weeks[4]
			w1,w2,w3,w4,w5=0,0,0,0,0
			for d in Monthly:
				if d['day'].day in week1_list:
					w1=w1+d['total']
				elif d['day'].day in week2_list:
					w2=w2+d['total']
				elif d['day'].day in week3_list:
					w3=w3+d['total']
				elif d['day'].day in week4_list:
					w4=w4+d['total']
				else:
					w5=w5+d['total']
			week1_setlist=list(set(week1_list))
			week2_setlist=list(set(week2_list))
			week3_setlist=list(set(week3_list))
			week4_setlist=list(set(week4_list))
			week5_setlist=list(set(week5_list))

			if 0 in week1_setlist:
				week1_setlist.remove(0)
			
			if 0 in week2_setlist:
				week2_setlist.remove(0)
			
			if 0 in week3_setlist:
				week3_setlist.remove(0)
			
			if 0 in week4_setlist:
				week4_setlist.remove(0)
			
			if 0 in week5_setlist:
				week5_setlist.remove(0)

			week1=str(week1_list[0])+'-'+str(month)+'-'+str(year)+' to '+str(week1_list[-1])+'-'+str(month)+'-'+str(year)
			week2=str(week2_list[0])+'-'+str(month)+'-'+str(year)+' to '+str(week2_list[-1])+'-'+str(month)+'-'+str(year)
			week3=str(week3_list[0])+'-'+str(month)+'-'+str(year)+' to '+str(week3_list[-1])+'-'+str(month)+'-'+str(year)
			week4=str(week4_list[0])+'-'+str(month)+'-'+str(year)+' to '+str(week4_list[-1])+'-'+str(month)+'-'+str(year)
			week5=str(week5_list[0])+'-'+str(month)+'-'+str(year)+' to '+str(week5_list[-1])+'-'+str(month)+'-'+str(year)

			labels=[week1,week2,week3,week4,week5]
			default=[w1,w2,w3,w4,w5]
			orders=Orders.objects.filter(orderdate__month=month).filter(orderdate__year=year).filter(restaurant_id=self.kwargs['pk']).order_by('-id')
			orderserializer=OrderSerializer(orders, many=True)
			total_list=[]
			for price in orders:
				total_list.append(float(price.totalpricetax))
			
			if total_list==[]:
				total=0
			else:
				total=sum(i for i in total_list)
			
			data={'labels':labels,'default':default,'orderserializer':orderserializer.data,'total':total }
			return Response(data)

class ImgDecode(View):
	def get(self,request, *args, **kwargs):
		today = datetime.now().date()
		month=today.month
		year=today.year
		start = today - timedelta(days=today.weekday())
		end = start + timedelta(days=6)
		id1=request.GET.get('id')
		selectvalue=request.GET.get('selectvalue')
		url_base64=request.GET.get('url_base64')
		path=request.get_full_path()
		waste,img=path.split('data:image/png;base64,')
		if selectvalue=='Weekly':
			orders=Orders.objects.filter(orderdate__range=[start, end]).filter(restaurant_id=id1).order_by('-id')
		elif selectvalue=='Quaterly':
			orders=Orders.objects.filter(orderdate__year=year).filter(restaurant_id=id1).order_by('-id')
		else:
			orders=Orders.objects.filter(orderdate__month=month).filter(orderdate__year=year).filter(restaurant_id=id1).order_by('-id')
		today_date=today.strftime('%d-%m-%Y')
		name=orders[0].restaurant.restaurantname
		total_list=[]
		for price in orders:
			total_list.append(float(price.totalpricetax))
		
		if total_list==[]:
			total=0
		else:
			total=sum(i for i in total_list)
		pdf = render_to_pdf('cart_and_orders/pdf1.html', {'image1':img,'selectvalue':selectvalue,'today_date':today_date,'orders':orders,'name':name,'total':total})
		return HttpResponse(pdf, content_type='application/pdf')
		
		
 