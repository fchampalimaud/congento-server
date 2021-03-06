from django.db import models

from model_utils import Choices


class Rodent(models.Model):

    # Fields shared with other congento animal models
    AVAILABILITIES = Choices(
        ("live", "Live"),
        ("cryo", "Cryopreserved"),
        ("both", "Live & Cryopreserved"),
        ("none", "Unavailable"),
    )

    created = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Updated", auto_now=True)
    availability = models.CharField(max_length=4, choices=AVAILABILITIES)
    link = models.URLField(blank=True)
    species = models.CharField(max_length=80)
    strain_name = models.CharField(max_length=20)
    common_name = models.CharField(max_length=20)
    origin = models.CharField(max_length=40)
    origin_other = models.CharField(max_length=40, blank=True)
    category = models.CharField(max_length=40)
    background = models.CharField(max_length=80, blank=True)
    zygosity = models.CharField(max_length=20, blank=True)
    line_description = models.TextField(blank=True)
    coat_color = models.CharField(max_length=40, blank=True)
    reporter_gene = models.CharField(max_length=40, blank=True)
    inducible_cassette = models.CharField(max_length=40, blank=True)

    remote_id = models.BigIntegerField("Remote ID")
    congento_member = models.ForeignKey(to="CongentoMember", on_delete=models.CASCADE)

    def __str__(self):
        return self.strain_name

    def get_institution_name(self):
        if self.congento_member.institution is None:
            return None
        else:
            return self.congento_member.institution.name

    get_institution_name.short_description = "Provider"
