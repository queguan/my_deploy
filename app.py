from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import Required, DataRequired


class NameForm(FlaskForm):
    verser_num = StringField('版本', description='示例：magic.r1.0.2.1.0615',validators=[DataRequired()])
    s_path = StringField('source path',description='示例：/data/package/magic.r1.0.2.1.0615/nginx.conf-magic.r1.0.2.1.0615', validators=[DataRequired()])
    d_path = StringField('destion path',description='示例： /data/nginx/conf/nginx.conf' ,validators=[DataRequired()])
    d_submit = SubmitField('发布')
    r_submit = SubmitField('回滚')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello world'
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('sara_index.html')


# @app.route('/deploy/<appname>')
# def deploy_app(appname):
#     deploy_name = "deploy_" + appname + ".html"
#     return render_template(deploy_name)

@app.route('/deploy/<appname>', methods=['GET', 'POST'])
def deploy_app(appname):
    version_num = None
    s_path = None
    deploy_name = "deploy_" + appname + ".html"
    form = NameForm()
    if form.validate_on_submit():
        session['version_num'] = form.verser_num.data
        session['s_path'] = form.s_path.data
        session['d_path'] = form.d_path.data
        return redirect(url_for('deploy_app',appname=appname))
    return render_template(deploy_name, form=form, output=session.get('version_num'))


if __name__ == '__main__':
    app.run(debug=True)
