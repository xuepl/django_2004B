# from django.db import models
#
# # Create your models here.
#
# class PhoneField(models.Field):  # 自定义的char类型的字段类
#
#     def __init__(self, max_length, *args, **kwargs):
#         self.max_length = max_length
#         super(PhoneField, self).__init__(max_length=max_length, *args, **kwargs)
#
#     def db_type(self, connection):  # 限定生成数据库表的字段类型为char，长度为max_length指定的值的字符串
#         return 'char(%s)' % self.max_length
#
# class Student(models.Model):
#     s_name = models.CharField(max_length=64,help_text="学生姓名")
#     s_sex = models.IntegerField(choices=((0,'男'),(1,'女')), help_text="性别")
#     s_phone = PhoneField(max_length=11,help_text="手机号")
#     # auto_now_add=True 在每一次数据被添加进去的时候，记录当前时间
#     create_time = models.DateTimeField(auto_now_add=True)
#     # auto_now=True 在每一次数据被保存的时候，记录当前时间
#     update_time = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table='student' # 指定表名
#         app_label="app02"
