from django.apps import apps as django_apps
from django.views.generic.base import ContextMixin
from edc_constants.constants import CLOSED
from edc_action_item.constants import RESOLVED, REJECTED


class ActionItemViewMixin(ContextMixin):

    action_item_model = 'edc_action_item.actionitem'
    action_item_model_wrapper_cls = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            action_items=self.action_items)
        return context

    def action_items(self):
        model_cls = django_apps.get_model(self.action_item_model)
        qs = model_cls.objects.filter(
            subject_identifier=self.kwargs.get('subject_identifier')).exclude(
                status__in=[RESOLVED, CLOSED, REJECTED]).order_by('-report_datetime')
        return [self.action_item_model_wrapper_cls(model_obj=obj) for obj in qs]
