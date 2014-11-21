"""TO-DO: Write a description of what this XBlock is."""

# import pudb;pudb.set_trace()
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment
from xblock_django.user_service import DjangoXBlockUserService

@XBlock.needs('user')
class ServicesDemoXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html = self.resource_string("static/html/services-demo-xblock.html")
        frag = Fragment(html.format(self=self))
        return frag

    @property
    def user_name(self):
        user = self.runtime.service(self, 'user').get_current_user()
        return user.full_name

    @property
    def user_email(self):
        user = self.runtime.service(self, 'user').get_current_user()
        return user.email

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Services Demo XBlock",
             """<vertical_demo>
                <xblockservicesdemo/>
                </vertical_demo>
             """),
        ]