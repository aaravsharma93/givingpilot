from .crowdfunding import *
from .new_campaign import *
import datetime


@login_required
def home_page(request):
    campaigns = Campaign.objects.select_related('owner').filter(is_published=True).order_by("organization_name")
    my_campaigns = [c for c in campaigns if c.owner == request.user]
    if len(my_campaigns)!=0:
        for obj in my_campaigns:
            if obj.has_end_date:
                obj.days=(obj.end_date-datetime.date.today()).days
                if obj.days < 0:
                    obj.days = 0
            else :
                obj.days = 0
    categories = utils.get_all_categories
    campaigns_by_cat = []
    for cat in categories:
        cat_campaign = campaigns.filter(category=cat)
        if len(cat_campaign)!=0:
            for obj in cat_campaign:
                if obj.has_end_date:
                    obj.days=(obj.end_date-datetime.date.today()).days
                    if obj.days < 0:
                        obj.days = 0
                else :
                    obj.days = 0
        campaigns_by_cat.append({
            "category": cat.id,
            "campaigns": cat_campaign
        })
    
    context = {
        'campaigns': Utils.get_all_published_campaigns(),
        'my_campaigns': my_campaigns,
        'categories': categories,
        'host': utils.get_protocol_and_host(request),
        'campaigns_by_cat': campaigns_by_cat
    }
    return render(request, 'dashboard/homepage/homepage_auth.html', context)


def home_page_public(request):
    campaigns = Campaign.objects.filter(is_published=True).order_by("-created_at")
    for obj in campaigns:
        if obj.has_end_date:
            obj.days=(obj.end_date-datetime.date.today()).days
            if obj.days < 0:
                obj.days = 0
        else :
            obj.days = 0
    categories = utils.get_all_categories
    campaigns_by_cat = []
    for cat in categories:
        cat_campaign = campaigns.filter(category=cat)
        if len(cat_campaign)!=0:
            for obj in cat_campaign:
                if obj.has_end_date:
                    obj.days=(obj.end_date-datetime.date.today()).days
                    if obj.days < 0:
                        obj.days = 0
                else :
                    obj.days = 0
        campaigns_by_cat.append({
            "category": cat.id,
            "campaigns": cat_campaign
        })

    context = {
        'campaigns': campaigns,
        'categories': categories,
        'host': utils.get_protocol_and_host(request),
        'campaigns_by_cat': campaigns_by_cat
    }
    return render(request, 'dashboard/homepage/homepage_public.html', context)


def pick_plan(request):
    return render(request, 'dashboard/new_campaign/pick_a_plan.html')
