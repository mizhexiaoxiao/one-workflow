# Generated by Django 3.0.3 on 2021-05-09 08:31

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(max_length=32, verbose_name='菜单名称')),
                ('code', models.CharField(max_length=32, verbose_name='菜单代码')),
                ('curl', models.CharField(max_length=101, verbose_name='菜单URL')),
                ('icon', models.CharField(blank=True, max_length=32, verbose_name='菜单图标')),
                ('hidden', models.BooleanField(default=False, verbose_name='菜单是否隐藏')),
                ('no_cache', models.BooleanField(default=True, verbose_name='菜单是否缓存')),
                ('active_menu', models.CharField(blank=True, max_length=32, verbose_name='激活菜单')),
                ('sequence', models.SmallIntegerField(default=0, verbose_name='排序值')),
                ('type', models.CharField(choices=[(1, '模块'), (2, '菜单'), (3, '操作')], default=2, max_length=1, verbose_name='菜单类型')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('operate', models.CharField(choices=[('none', '无'), ('add', '新增'), ('del', '删除'), ('update', '编辑'), ('view', '查看')], default='none', max_length=11, verbose_name='操作类型')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.Menu', verbose_name='父级菜单')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('code', models.CharField(max_length=32, unique=True, verbose_name='代码')),
                ('sequence', models.SmallIntegerField(default=0, verbose_name='排序值')),
                ('menus', models.ManyToManyField(blank=True, to='systems.Menu', verbose_name='菜单')),
                ('model_perms', models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='model权限')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.Role', verbose_name='父级角色')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('code', models.CharField(max_length=32, unique=True, verbose_name='代码')),
                ('sequence', models.SmallIntegerField(default=0, verbose_name='排序值')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.Group', verbose_name='父级角色')),
                ('roles', models.ManyToManyField(blank=True, to='systems.Role', verbose_name='roles')),
            ],
            options={
                'verbose_name': '分组',
                'verbose_name_plural': '分组',
            },
            bases=('auth.group', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('username', models.CharField(db_index=True, max_length=32, unique=True)),
                ('realname', models.CharField(blank=True, default='图书馆管理员', max_length=32, verbose_name='真实名字')),
                ('email', models.EmailField(blank=True, default='itimor@126.com', max_length=254, verbose_name='邮箱')),
                ('avatar', models.CharField(default='http://m.imeitou.com/uploads/allimg/2017110610/b3c433vwhsk.jpg', max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_set', related_query_name='user', to='systems.Group', verbose_name='group')),
                ('model_perms', models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('roles', models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='systems.Role', verbose_name='roles')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
