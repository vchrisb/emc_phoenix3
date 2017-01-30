from django.conf import settings
from django.shortcuts import render, get_object_or_404
from phoenix.decorators import specific_verified_email_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from .models import Badge, CrawledBadge
from guardian.shortcuts import get_objects_for_user
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import pyotp

# Create your views here.
#@specific_verified_email_required(domains=settings.ALLOWED_DOMAINS)
@login_required
def qrcode(request, uuid):
    BadgeObj = get_object_or_404(Badge, pk=uuid)
    UserObj = User.objects.get(username=request.user)
    if not UserObj.has_perm('view_badge_secret', BadgeObj):
        return HttpResponseForbidden()
    
    context = {
        "BadgeObj": BadgeObj
    }

    return render(request, "boothcrawl/qrcode.html", context)
@login_required
def qrcodes(request):
    BadgeObj = get_objects_for_user(request.user, 'boothcrawl.view_badge_secret', with_superuser=True)    
    context = {
        "badges": BadgeObj
    }

    return render(request, "boothcrawl/qrcodes.html", context)
 
@specific_verified_email_required(domains=settings.ALLOWED_DOMAINS)
def crawl(request, uuid, otp):
    BadgeObj = get_object_or_404(Badge, pk=uuid)
    totp = pyotp.TOTP(BadgeObj.secret_key)
    if totp.verify(otp, valid_window = 1):
        print("success")
        CrawledBadgeObj, created = CrawledBadge.objects.get_or_create(user=request.user, badge=BadgeObj)
        status = "Successfully achieved Badge for " + BadgeObj.name + " !"
        status_code = "success"
        if not created:
            status = "Badge for " + BadgeObj.name + " already achieved on " + timezone.localtime(CrawledBadgeObj.achieved_at).strftime("%H:%M:%S %d %b %Y") + "!"
            status_code = "warning"
    else:
        status = "Access code for Badge " + BadgeObj.name + " expired! Please rescan QR code!"
        status_code = "danger"
        
    context = {
        "status": status,
        "status_code": status_code
    }

    return render(request, "boothcrawl/crawl.html", context)
    
@specific_verified_email_required(domains=settings.ALLOWED_DOMAINS)
def badges(request):
    CrawledBadgeObj = CrawledBadge.objects.filter(user=request.user)
    
    context = {
        "CrawledBadges": CrawledBadgeObj,
        "nr_crawled": CrawledBadgeObj.count(),
        "total_badges": Badge.objects.count()
    }
    return render(request, "boothcrawl/badges.html", context)

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
import random
@staff_member_required
def crawl_score_list(request):
    total_badges = Badge.objects.count()
    CrawledBadgeList = CrawledBadge.objects.all().values('user', 'user__first_name', 'user__last_name').annotate(total=Count('user')).filter(total=total_badges).order_by('user__last_name')
    crawl_winner = ''
    if CrawledBadgeList.exists():
        randomcrawl = random.randrange(0,CrawledBadgeList.count())
        crawl_winner = CrawledBadgeList[randomcrawl]
    
    context = {
        "crawl_winner": crawl_winner,
        "CrawledBadgeList": CrawledBadgeList
    }
    return render(request, "boothcrawl/crawlscorelist.html", context)