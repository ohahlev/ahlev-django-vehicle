from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from imagekit import ImageSpec
from imagekit.processors import ResizeToFit, SmartResize
from imagekit.cachefiles import ImageCacheFile

class AdminSmallestThumbnailSpec(ImageSpec):
    processors = [ResizeToFit(None, 50)]
    format = 'PNG'
    options = {'quality': 60 }

class AdminSmallThumbnailSpec(ImageSpec):
    processors = [ResizeToFit(300)]
    format = 'PNG'
    options = {'quality': 60 }

def cached_admin_thumb_in_edit(instance):
    cached = ImageCacheFile(AdminSmallThumbnailSpec(instance))
    cached.generate()
    return cached

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        print(value)
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            thumbnail = cached_admin_thumb_in_edit(value)
            output.append(u'<a href="%s" target="_blank"><img src="%s" alt="%s" width="400" style="object-fit: cover;"/></a> %s ' % \
            (image_url, thumbnail.url, file_name, _('')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

