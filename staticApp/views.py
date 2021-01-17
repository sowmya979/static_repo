from django.shortcuts import render
def view1(request):
   myName="Sowmya"
   favPlayer="ABD"
   favAnimal="Lion"
   favSubject="Pyhton"
   d={"Name":myName,"Player":favPlayer,"Animal":favAnimal,"Subject":favSubject}
   return render(request,'staticApp/1.html',d)