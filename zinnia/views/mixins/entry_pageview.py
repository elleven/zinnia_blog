"""Page view mixin for Zinnia views"""


class EntryPageViewMixin(object):

    """
    Mixin implementing the page views of Entries.
    """
    def get_object(self, queryset=None):
        """
        when the entry is viewed ,page view +1
        """
        obj = super(EntryPageViewMixin, self).get_object(queryset)
        obj.page_view += 1
        obj.save()
        return obj
