from django.db import migrations
from django.conf import settings


def update_site_name(apps, schema_editor):
    SiteModel = apps.get_model('sites', 'Site')
    domain = 'mydomain.com'

    SiteModel.objects.update_or_create(
        settings.SITE_ID,
        {'domain': domain, 'name': domain}
    )


class Migration(migrations.Migration):

    dependencies = [
        # Make sure the dependency that was here by default is also included here
        ('sites', '0002_alter_domain_unique'), # Required to reference `sites` in `apps.get_model()`
    ]

    operations = [
        migrations.RunPython(update_site_name),
    ]