# WIZ Framework

- WIZ is IDE for web development
- Using angular more easy

![screenshot](https://github.com/season-framework/wiz/blob/main/screenshot/wiz.gif)

## Installation

- install nodejs, npm, angular

```bash
apt install nodejs npm
npm i -g n
n stable
```

- install wiz python package

```bash
pip install season             # install
pip install season --upgrade   # upgrade lastest
```

## Usage

- create project

```bash
cd <workspace>
wiz create myapp
cd myapp
wiz run --port 3000
```

> `http://127.0.0.1:3000/wiz` on your web browser

- create from git repo

```bash
wiz create myapp --uri=https://your-custom/git/project
```

- daemon server

```bash
wiz server start # start daemon server
wiz server stop  # stop daemon server
```

- upgrade ide from command line

```bash
pip install season --upgrade # upgrade core
wiz ide upgrade # ide upgrade
wiz server stop
wiz server start --log wiz.log
```

- install ide plugin

```bash
wiz plugin add https://github.com/season-framework/wiz-plugin-xterm
```

## Version Info

> x.y.z

- `x`: major update
    - upgrade not supported
- `y`: minor update
    - support command upgrade
    - core function changed
    - required server restart
- `z`: ui update
    - support upgrade from web ui
    - not required server restart

## Release Note

### 2.2.5

- [core] angular version upgrade

### 2.2.4

- [core] toastr on build error 
- [plugin/workspace] hidden portal framework on route
- [plugin/workspace] image viewer

### 2.2.3

- [plugin/workspace] Usability improvements
- [plugin/core] Auto Complete keyword

### 2.2.2

- [core] ide monaco editor bug fixed

### 2.2.1

- [plugin/portal] add portal framework plugin
- [plugin/workspace] refresh list bug fixed

### 2.2.0

- ide overlay menu
- shortcut config (plugin & user customized)

### 2.1.x

- major issues
    - ide plugin concept changed
    - ide layout changed
    - ide config concept added
- [plugin/core] move to app link in monaco editor
- [plugin/core] add core plugins upgrade button
- [plugin/core] add restart server button
- [plugin/workspace] add app/route editor service
- [plugin/workspace] preview bug fixed
- [plugin/workspace] page namespace bug fixed
- [plugin/workspace] set default code if component.ts not exists
- [plugin/workspace] import & create app bug fixed
- [plugin/core] remove useless log
- [plugin/workspace] config folder bug fixed
- [plugin] bug fixed (remove unused file)
- [plugin/workspace] add route build
- [plugin/workspace] remove useless log
- [plugin] `core` plugin updated
- [core] add `lib/plugin` object
- [command] bug fixed

### 2.0.x

- major issues
    - upgrade base project to angular 14.2.0
    - UI/UX full changed
    - Drag and Drop Interface
    - git branch to project (multiple project in workspace)
    - Enhanced IDE Plugin and easily develop 3rd party apps
    - support pip and npm on ui
- ide socket
- auto install `@angular/cli`
- angular 15
- flask response bug fixed (on filesend)
- wiz bundle mode
- update wiz server command (multiprocess)
- config bug fixed
- socketio bug fixed (ide controller)
- threading bug fixed (flask, socketio)

### 1.0.x

- major issue
    - clean code
    - full changed ide
    - remove season-flask concept
    - enhanced performance
    - logging for wiz concept
    - upgrade plugin structure
    - config structure changed
    - stable version for git merge
- add `wiz server start --log <file>` method 
- print bug fixed
- add daemon server command
- Socket.IO transport
- server starting log
- auto remove invalid character on update
- WSGI Bug Fixed
- remove dukpy (windows install bug)
- support macosx

### 0.5.x

- support plugin storage
- port scan when wiz project created
- wiz based online plugin development env
- support programmable api for plugins
- remove useless resources
- socketio config (config/socketio.py)
- packages version bug fixed (jinja2, werkzeug)
- add src folder for tracing plugin code
- check installed function (wiz.installed())
- forced dev mode in dev branch (if not master)
- wiz `resource_handler` updated
- add function response(flask_resp) and pil_image at `response`
- add babel script option
- add `wiz.path()` function
- git merge bug fixed
- update wiz theme render logic
- git merge logic changed
- wiz instance as global in wiz api
- add `match` api at wiz instance

### 0.4.x

- Integrate WIZ & Season Flask
- support git flow
- workspace structure changed
- base code workspace changed (mysql to filesystem)
- UI upgrade
- support installer
- developer/production mode
    - developer: enabled socketio logger on every pages
    - production: disabled socketio logger
- dictionary bug fixed in App HTML
- history display ui changed (workspace)
- app browse in route workspace
- add cache clean in workspace
- git bug changed (if author is not set, default user to `wiz`)
- full size log viewer
- keyword changed
- cache bug fixed
- socketio performance upgrade 
- wiz.js embeded
- WIZ API (js) changed (async mode)

### 0.3.x

- add socket.io 
- framework on build
- command run modified (add pattern, ignores)
- change Framework Object

### 0.2.x

- framework structure upgraded
- command line tool function changed
- submodule structure added
- logging 
- simplify public directory structure
- add response.template_from_string function
- add response.template function
- add variable expression change option
- interface loader update
- config onerror changed 
- add response.abort
- error handler in controller `__error__`
- response redirect update (relative module path)
- logger upgrade (file trace bug fixed)
- logger upgrade (log executed file trace)
- logger upgrade (code trace)
- error handler bug fixed
- apache wsgi bug fixed (public/app.py)
- apache wsgi bug fixed
