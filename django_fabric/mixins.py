import os

from fabric.api import cd
from fabric import colors
from fabric.contrib.console import confirm
from fabric.contrib.files import exists


class VirtualenvMixin(object):
    """
    A mixin that will check for a virtualenvironment at <project_path>/venv
    before deployment.
    """

    def run_server_updates(self, instance):
        code_dir = self.project_paths[instance]
        self.check_virtualenv(code_dir)
        super(VirtualenvMixin, self).run_server_updates(instance)

    def check_virtualenv(self, path):
        venv_path = os.path.join(path, "venv")
        if not exists(venv_path):
            if confirm("virtualenv not found. Do you want to create one"):
                print(colors.yellow("Creating virtualenv"))
                with cd(path):
                    self.run("virtualenv venv")