Django的content-type组件
======

## content-type
- Django的内置的一个组件，帮助开发者做连表操作【混搭】
    - content-type可以自动的创建一张表，存储关联的表名，这个适用于多表关联的情况
    - 提供了GenericForeignKey帮助我们快速的插入数据
    - 使用GenericRelation查找，查找某个东西的时候，可以查出全部与之相关的内容，这个仅用于反向查找

