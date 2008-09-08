from django.db import models
from django.db.models.query import QuerySet


class ChildQuerySet(QuerySet):
    def iterator(self):
        for obj in super(ChildQuerySet, self).iterator():
            yield obj.get_child_object()


class ChildManager(models.Manager):
    def get_query_set(self):
        return ChildQuerySet(self.model)


class ParentModel(models.Model):
    _child_name = models.CharField(max_length=100, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self._child_name = self.get_child_name()
        super(ParentModel, self).save(*args, **kwargs)

    def get_child_name(self):
        if type(self) is self.get_parent_model():
            return self._child_name
        return self.get_parent_link().related_query_name()

    def get_child_object(self):
        return getattr(self, self.get_child_name())

    def get_parent_link(self):
        return self._meta.parents[self.get_parent_model()]

    def get_parent_model(self):
        raise NotImplementedError

    def get_parent_object(self):
        return getattr(self, self.get_parent_link().name)
