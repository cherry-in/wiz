import os
import season
import json

class Controller(season.interfaces.wiz.ctrl.admin.plugin.api):

    def __startup__(self, framework):
        super().__startup__(framework)

    def list(self, framework):
        rows = self.plugin.list()
        framework.response.status(200, rows)

    def create(self, framework):
        plugin_info = framework.request.query()
        self.wiz.data.create_plugin(plugin_info)
        framework.response.status(200)

    def info(self, framework):
        plugin_id = framework.request.segment.get(0, True)
        info = self.plugin.get(plugin_id)
        if info is None:
            framework.response.status(404)
        framework.response.status(200, info)

    def update(self, framework):
        info = framework.request.query("info", True)
        info = json.loads(info)
        self.wiz.data.update(info, mode='plugin')
        framework.response.status(200)

    def delete(self, framework):
        app_id = framework.request.segment.get(0, True)
        self.wiz.data.delete(app_id, mode='plugin')
        framework.response.status(200)

    def history(self, framework):
        commits = framework.wiz.workspace.commits(branch=None, max_count=100)
        framework.response.status(200, commits)

    def diff(self, framework):
        app_id = framework.request.segment.get(0, True)
        commit = framework.request.segment.get(1, True)
        filepath = f'apps/{app_id}'

        def load_app_files(key):
            try:
                appfile = os.path.join(filepath, key)
                text = framework.wiz.workspace.file(appfile, branch=None, commit=commit)
                return text
            except:
                return ""

        appinfo = dict()
        appinfo = os.path.join(filepath, 'app.json')
        appinfo = framework.wiz.workspace.file(appinfo, branch=None, commit=commit)
        appinfo_txt = appinfo
        appinfo = json.loads(appinfo)
        appinfo['info'] = appinfo_txt
        appinfo['code'] = dict()
        appinfo['code']["controller"] = load_app_files("controller.py")
        appinfo['code']["dic"] = load_app_files("dic.json")
        appinfo['code']["api"] = load_app_files("api.py")
        appinfo['code']["socketio"] = load_app_files("socketio.py")
        appinfo['code']["html"] = load_app_files("html.dat")
        appinfo['code']["js"] = load_app_files("js.dat")
        appinfo['code']["css"] = load_app_files("css.dat")

        framework.response.status(200, appinfo)