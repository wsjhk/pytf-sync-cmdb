terraform import导入存量资源的步骤：

    1)使用datasource定义查询；
    2)使用output将查询结果输出；
    3)使用apply执行拿到结果（注意apply执行前确保只有datasource和output的定义，不要定义resource资源，否则会导致云上资源被更新的情况）；
    4)python将拿到的结果进行处理后保存；
    5)声明要导入资源resource的模板,由于resource是唯一的，所以需要根据结果id的数量创建对应的数量的resource和对应关系；
    6)根据python保存的结果资源ID和其对应声明的资源模板，使用terraform import命令进行导入；
    7)导入完成后使用python实现模板资源定义的补齐；
    8)使用terraform plan验证补齐结果，完成导入。


待开发功能：

    1)集成多账号，多区域，多云资源的查询获取；
    2)使用多线程或者协程处理数据发送到kafka；
    3)添加异常处理和日志打印；
    4)配置参数通过文件配置；
    5)其他优化，如：tfstate文件存储管理。


