from django.contrib.sitemaps import Sitemap
from jobs.models import Jobs

class JobSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Jobs.objects.all().order_by('-created_at')  # Order by created_at in descending order

    def lastmod(self, obj):
        return obj.created_at  # Use created_at for lastmod if applicable
