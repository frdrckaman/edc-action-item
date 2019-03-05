from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from edc_constants.choices import YES_NO
from edc_constants.constants import YES
from edc_model.models import BaseUuidModel
from edc_model.models import HistoricalRecords
from edc_sites.models import SiteModelMixin
from edc_utils import get_utcnow

from ..models import ActionModelMixin


class SubjectIdentifierModelManager(models.Manager):
    def get_by_natural_key(self, subject_identifier):
        return self.get(subject_identifier=subject_identifier)


class SubjectIdentifierModel(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    objects = SubjectIdentifierModelManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,)


class TestModelWithoutMixin(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)
    history = HistoricalRecords()


class TestModelWithActionDoesNotCreateAction(ActionModelMixin, BaseUuidModel):

    action_name = "test-nothing-prn-action"


class TestModelWithAction(ActionModelMixin, BaseUuidModel):

    action_name = "submit-form-zero"


class Appointment(BaseUuidModel):

    appt_datetime = models.DateTimeField(default=get_utcnow)
    history = HistoricalRecords()


class SubjectVisit(SiteModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    appointment = models.OneToOneField(Appointment, on_delete=CASCADE)
    history = HistoricalRecords()


class FormZero(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    action_name = "submit-form-zero"

    f1 = models.CharField(max_length=100, null=True)


class FormOne(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    action_name = "submit-form-one"

    f1 = models.CharField(max_length=100, null=True)


class FormTwo(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    form_one = models.ForeignKey(FormOne, on_delete=PROTECT)

    action_name = "submit-form-two"


class FormThree(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    action_name = "submit-form-three"


class FormFour(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    action_name = "submit-form-four"

    happy = models.CharField(max_length=10, choices=YES_NO, default=YES)


class Initial(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    action_name = "submit-initial"


class Followup(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    initial = models.ForeignKey(Initial, on_delete=CASCADE)

    action_name = "submit-followup"


class MyAction(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    action_name = "my-action"


class CrfOne(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    subject_visit = models.OneToOneField(SubjectVisit, on_delete=CASCADE)

    action_name = "submit-crf-one"

    @property
    def visit(self):
        return self.subject_visit

    @classmethod
    def visit_model_attr(self):
        return "subject_visit"


class CrfTwo(ActionModelMixin, SiteModelMixin, BaseUuidModel):

    subject_visit = models.OneToOneField(SubjectVisit, on_delete=CASCADE)

    action_name = "submit-crf-two"

    @property
    def visit(self):
        return self.subject_visit

    @classmethod
    def visit_model_attr(self):
        return "subject_visit"
