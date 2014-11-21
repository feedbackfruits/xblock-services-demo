"""A simple XBlock demoing the data that the user and course services expose"""

# import pudb;pudb.set_trace()
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment

@XBlock.needs('user')
@XBlock.needs('course')
class ServicesDemoXBlock(XBlock):
    """
    A simple XBlock demoing the data that the user and course services expose
    """

    display_name=String(
        default="XBlock Services Demo",
        scope=Scope.settings
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html = self.resource_string("static/html/services-demo-xblock.html")
        frag = Fragment(html.format(self=self))
        return frag

    @property
    def user(self):
        return self.runtime.service(self, 'user').get_current_user()

    @property
    def course(self):
        return self.runtime.service(self, 'course').get_current_course()

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