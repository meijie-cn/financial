# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import User_Info
from django.contrib.auth.models import User
from . import tasks 

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    
    if request.method == "POST":
        # save profile edit
        if "SaveProfile" in request.POST:
            # get new info
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            address = request.POST.get("address")
            city = request.POST.get("city")
            country = request.POST.get("country")
            postal_code = request.POST.get("postal_code")
            about_me = request.POST.get("about_me")
            
            #get object
            pf_user = User.objects.get(pk=request.user.id)
            pf_info = User_Info.objects.get(user=request.user)
            
            #update
            pf_user.email=email
            pf_user.first_name=first_name
            pf_user.last_name=last_name
            
            pf_info.contact_address=address
            pf_info.contact_city=city
            pf_info.contact_country=country
            pf_info.contact_postalcode=postal_code
            pf_info.about_me=about_me
            
            #save
            pf_info.save()
            pf_user.save()
        
        if "refresh-stock" in request.POST:
            tasks.update_sz_all_stocks()
            
        
        if "refresh-trends" in request.POST:
            
            pass
        
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
    
        if request.method == "GET":
            if "edit" in request.GET:
                context['edit_mode'] = "Y"
                
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        if "profile" in load_template:
            info = User_Info.objects.get(user=request.user)
            print("get info, id=" + str(info.id))
            context['info'] = info
                    
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))  
            
    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))
        
    except Exception:
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
    