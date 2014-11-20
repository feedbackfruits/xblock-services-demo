"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment
from xblock.references.plugins.services import UserService

@XBlock.needs('UserService')
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
        user_service = self.runtime.service(self, 'UserService')
        return user_service.name();

    @property
    def user_email(self):
        user_service = self.runtime.service(self, 'UserService')
        return user_service.email();

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