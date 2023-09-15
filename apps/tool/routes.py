# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 FutureX. All rights reserved.

"""

from flask import render_template, redirect, request, url_for,session

from apps.tool import blueprint
from apps.tool.forms import LoginForm
from apps.tool.writingTool import dataJson
from flask import render_template, request
from flask_login import login_required





@blueprint.route('/tool')
@login_required
def tool():
    toolName = request.args.get('name')
    data=dataJson[toolName]
    print(data)
    login_form = LoginForm(request.form)
    return render_template("tool/tool.html",form=login_form,ToolData =data,classMarch=getattr)
