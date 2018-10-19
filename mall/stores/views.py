from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from . import models


#增加店铺
@login_required()
def add(request):
	if request.mthod == "GET":
		return render(request, "store/add.html", {})
	else:
		name = request.POST["name"].strip()
		intro = request.POST["intro"].strip()

		try:
			cover = request.FILES["cover"]
			store = models.Stores(name=name, intro=intro, cover=cover, user=request.user)
		except:
			store = models.Stores(name=name, intro=intro, user=request.user)
		store.save()

		return redirect(reverse("store:detail", kwargs={"s_id": store.id}))


#查询店铺
@require_GET
@login_required()
def list(request):
	stores = models.Stores.objects.filter(user=request.user, status_int=[0, 1])
	return render(request, "store/list.html", {"stores": stores})


#修改店铺
@require_GET
@login_required()
def update(request, s_id):
	if request.mthod == "GET":
		store = models.Stores.objects.get(pk=s_id)
		return render(request, "store/update.html", {"store":store})
	else:
		name = request.POST["name"].strip()
		intro = request.POST["intro"].strip()

		store = models.Stores.objects.get(pk=s_id)
		store.name = name
		store.intro = intro

		try:
			cover = request.FILES["cover"]
			store.cover = cover
		except:
			pass
		store.save()

		return redirect(reverse("store:detail", kwargs={"s_id": store.id}))



#店铺详情
@require_GET
@login_required()
def detail(request, s_id):
	store = models.Stores.objects.get(pk=s_id)
	return render(request, "store/detail.html", {"store": store})


#关闭店铺
@require_GET
@login_required()
def change(request, s_id, status):
	store = models.Stores.objects.get(pk=s_id)
	store.status = int(status)
	store.save()
	if store == 2:
		return redirect(reverse("store:list"))
	else:
		return render(request, "store/detail.html", {"store": store})