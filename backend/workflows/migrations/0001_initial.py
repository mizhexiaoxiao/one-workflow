# Generated by Django 3.0.3 on 2021-06-16 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('field_attribute', models.BooleanField(default=False, verbose_name='字段是否内置')),
                ('field_type', models.CharField(choices=[(1, '字符串'), (2, '整型'), (3, '浮点型'), (4, '布尔'), (5, '日期'), (6, '日期时间'), (7, '范围日期'), (8, '文本域'), (9, '单选框'), (10, '下拉列表'), (11, '用户名'), (12, '多选框'), (13, '多选下拉'), (14, '多选用户名')], default=0, max_length=1, verbose_name='字段类型')),
                ('field_key', models.CharField(help_text='字段类型请尽量特殊，避免与系统中关键字冲突', max_length=50, verbose_name='字段标识')),
                ('field_name', models.CharField(max_length=50, verbose_name='字段名称')),
                ('order_id', models.IntegerField(default=0, verbose_name='排序')),
                ('default_value', models.CharField(blank=True, help_text='前端展示时，可以将此内容作为表单中的该字段的默认值', max_length=100, null=True, verbose_name='默认值')),
                ('field_template', models.TextField(blank=True, default='', help_text='文本域类型字段前端显示时可以将此内容作为字段的placeholder', verbose_name='文本域模板')),
                ('boolean_field_display', models.CharField(blank=True, default='{}', help_text='当为布尔类型时候，可以支持自定义显示形式。{"1":"是","0":"否"}或{"1":"需要","0":"不需要"}，注意数字也需要引号', max_length=100, verbose_name='布尔类型显示名')),
                ('field_choice', models.CharField(blank=True, default='{}', help_text='radio,checkbox,select,multiselect类型可供选择的选项，格式为json如:{"1":"中国", "2":"美国"},注意数字也需要引号', max_length=255, verbose_name='radio、checkbox、select的选项')),
                ('label', models.CharField(blank=True, default='{}', help_text='自定义标签，json格式，调用方可根据标签自行处理特殊场景逻辑，loonflow只保存文本内容', max_length=100, verbose_name='标签')),
            ],
            options={
                'verbose_name': '工作流自定义字段',
                'verbose_name_plural': '工作流自定义字段',
                'ordering': ['order_id'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('is_hidden', models.BooleanField(default=False, help_text='设置为True时,获取工单步骤api中不显示此状态(当前处于此状态时除外)', verbose_name='是否隐藏')),
                ('order_id', models.IntegerField(default=1, verbose_name='状态顺序')),
                ('state_type', models.CharField(choices=[(0, '普通状态'), (1, '初始状态'), (2, '结束状态')], default=0, max_length=1, verbose_name='状态类型')),
                ('enable_retreat', models.BooleanField(default=False, help_text='开启后允许工单创建人在此状态直接撤回工单到初始状态', verbose_name='允许撤回')),
                ('participant_type', models.CharField(choices=[('none', '无处理人'), ('user', '个人'), ('group', '部门'), ('role', '角色')], default='none', max_length=5, verbose_name='参与者类型')),
                ('fields', models.ManyToManyField(blank=True, to='workflows.CustomField', verbose_name='可编辑字段')),
                ('group_participant', models.ManyToManyField(blank=True, to='systems.Group', verbose_name='参与组')),
                ('role_participant', models.ManyToManyField(blank=True, to='systems.Role', verbose_name='参与角色')),
                ('user_participant', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='参与用户')),
            ],
            options={
                'verbose_name': '工作流状态',
                'verbose_name_plural': '工作流状态',
                'ordering': ['order_id'],
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('key', models.CharField(blank=True, max_length=168, verbose_name='流程标识key')),
                ('ticket_sn_prefix', models.CharField(default='xxoo', max_length=20, verbose_name='工单流水号前缀')),
                ('status', models.BooleanField(default=True)),
                ('view_permission_check', models.BooleanField(default=True, help_text='开启后，只允许工单的关联人(创建人、曾经的处理人)有权限查看工单', verbose_name='查看权限校验')),
                ('limit_expression', models.TextField(blank=True, default='{}', help_text='限制周期({"period":24} 24小时), 限制次数({"count":1}在限制周期内只允许提交1次), 限制级别({"level":1} 针对(1单个用户 2全局)限制周期限制次数,默认特定用户);允许特定人员提交({"allow_persons":"zhangsan,lisi"}只允许张三提交工单,{"allow_depts":"1,2"}只允许部门id为1和2的用户提交工单，{"allow_roles":"1,2"}只允许角色id为1和2的用户提交工单)', verbose_name='限制表达式')),
                ('display_form_str', models.TextField(blank=True, default='[]', help_text='默认"[]"，用于用户只有对应工单查看权限时显示哪些字段,field_key的list的json,如["days","sn"],内置特殊字段participant_info.participant_name:当前处理人信息(部门名称、角色名称)，state.state_name:当前状态的状态名,workflow.workflow_name:工作流名称', verbose_name='展现表单字段')),
                ('title_template', models.CharField(blank=True, default='你有一个待办工单:{title}', help_text='工单字段的值可以作为参数写到模板中，格式如：你有一个待办工单:{title}', max_length=50, null=True, verbose_name='标题模板')),
                ('roles', models.ManyToManyField(blank=True, related_name='workflow_set', related_query_name='workflow', to='systems.Role', verbose_name='关联角色')),
            ],
            options={
                'verbose_name': '工作流',
                'verbose_name_plural': '工作流',
            },
        ),
        migrations.CreateModel(
            name='WorkflowType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('status', models.BooleanField(default=True)),
                ('code', models.CharField(max_length=32, unique=True, verbose_name='代码')),
                ('order_id', models.IntegerField(default=1, verbose_name='状态顺序')),
            ],
            options={
                'verbose_name': '工作流类型',
                'verbose_name_plural': '工作流类型',
                'ordering': ['order_id'],
            },
        ),
        migrations.CreateModel(
            name='WorkflowBpmn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('xml', models.TextField(blank=True, verbose_name='xml数据')),
                ('svg', models.TextField(blank=True, verbose_name='svg数据')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.Workflow', verbose_name='工作流')),
            ],
            options={
                'verbose_name': '工作流bpmn',
                'verbose_name_plural': '工作流bpmn',
            },
        ),
        migrations.AddField(
            model_name='workflow',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.WorkflowType', verbose_name='工作流类型'),
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(choices=[(0, '保存'), (1, '转交下一步'), (2, '驳回'), (3, '撤销'), (4, '关闭')], default=1, max_length=1, verbose_name='名称类型')),
                ('transition_type', models.CharField(choices=[(0, '常规流转'), (1, '定时器流转')], default=0, max_length=1, verbose_name='流转类型')),
                ('timer', models.IntegerField(default=0, help_text='流转类型设置为定时器流转时生效,单位秒。处于源状态X秒后如果状态都没有过变化则自动流转到目标状态', verbose_name='定时器(单位秒)')),
                ('condition_expression', models.TextField(default='[]', help_text='流转条件表达式，根据表达式中的条件来确定流转的下个状态，格式为[{"expression":"{days} > 3 and {days}<10", "target_state_id":11}] 其中{}用于填充工单的字段key,运算时会换算成实际的值，当符合条件下个状态将变为target_state_id中的值,表达式只支持简单的运算或datetime/time运算.loonflow会以首次匹配成功的条件为准，所以多个条件不要有冲突', verbose_name='条件表达式')),
                ('attribute_type', models.CharField(choices=[(0, '草稿'), (1, '待审'), (2, '驳回'), (3, '撤销'), (4, '结束'), (5, '已关闭')], default=0, max_length=1, verbose_name='属性类型')),
                ('alert_enable', models.BooleanField(default=False, verbose_name='点击弹窗提示')),
                ('alert_text', models.CharField(blank=True, default='', max_length=100, verbose_name='弹窗内容')),
                ('dest_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dest_state', to='workflows.State', verbose_name='目的状态')),
                ('source_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source_state', to='workflows.State', verbose_name='源状态')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.Workflow', verbose_name='工作流')),
            ],
            options={
                'verbose_name': '工作流流转',
                'verbose_name_plural': '工作流流转',
            },
        ),
        migrations.AddField(
            model_name='state',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.Workflow', verbose_name='工作流'),
        ),
        migrations.AddField(
            model_name='customfield',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.Workflow', verbose_name='工作流'),
        ),
    ]
