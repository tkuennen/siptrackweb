from django.conf.urls import url
from siptrackweb import views
from siptrackweb.views import root
from siptrackweb.views import display
from siptrackweb.views import view
from siptrackweb.views import attribute
from siptrackweb.views import template
from siptrackweb.views import counter
from siptrackweb.views import network
from siptrackweb.views import device
from siptrackweb.views.device import config as device_config
from siptrackweb.views.device import config_template as device_config_template
from siptrackweb.views.device import network as device_network
from siptrackweb.views.device import device_association
from siptrackweb.views import password
from siptrackweb.views import user
from siptrackweb.views import config
from siptrackweb.views import permission
from siptrackweb.views import command
from siptrackweb.views import event


urlpatterns = [
    url(r'^$', root.index, name='siptrackweb.views.root.index'),
    url(r'^404$', root.p404, name='siptrackweb.views.root.p404'),

    url(r'^display/(?P<oid>[^/]+)/$', display.display, name='siptrackweb.views.display.display'),

    url(r'^view/$', view.index, name='siptrackweb.views.view.index'),
    url(r'^view/add/$', view.add, name='siptrackweb.views.view.add'),
    url(r'^view/add/post/$', view.add_post, name='siptrackweb.views.view.add_post'),
    url(r'^view/delete/(?P<oid>[^/]+)/$', view.delete, name='siptrackweb.views.view.delete'),
    url(r'^view/delete/post/(?P<oid>[^/]+)/$', view.delete_post,
        name='siptrackweb.views.view.delete_post'),
    url(r'^view/update/(?P<oid>[^/]+)/$', view.update, name='siptrackweb.views.view.update'),
    url(r'^view/update/post/(?P<oid>[^/]+)/$', view.update_post,
        name='siptrackweb.views.view.update_post'),
    url(r'^view/display/(?P<oid>[^/]+)/$', view.display, name='siptrackweb.views.view.display'),

    url(r'^attribute/add/select/(?P<target_oid>[^/]+)/$', attribute.add_select,
        name='siptrackweb.views.attribute.add_select'),
    url(r'^attribute/add/set/(?P<target_oid>[^/]+)/$', attribute.add_set,
        name='siptrackweb.views.attribute.add_set'),
    url(r'^attribute/add/post/(?P<target_oid>[^/]+)/$', attribute.add_post,
        name='siptrackweb.views.attribute.add_post'),
    url(r'^attribute/update/(?P<oid>[^/]+)/$', attribute.update,
        name='siptrackweb.views.attribute.update'),
    url(r'^attribute/update/post/(?P<oid>[^/]+)/$', attribute.update_post,
        name='siptrackweb.views.attribute.update_post'),
    url(r'^attribute/delete/(?P<oid>[^/]+)/$', attribute.delete,
        name='siptrackweb.views.attribute.delete'),
    url(r'^attribute/display/(?P<oid>[^/]+)/$', attribute.display,
        name='siptrackweb.views.attribute.display'),
    url(r'^attribute/notes/(?P<oid>[^/]+)/$', attribute.edit_notes,
        name='siptrackweb.views.attribute.edit_notes'),
    url(r'^attribute/notes/post/(?P<oid>[^/]+)/$', attribute.edit_notes_post,
        name='siptrackweb.views.attribute.edit_notes_post'),
    url(r'^attribute/quickedit/(?P<attr_name>[^/]+)/(?P<oid>[^/]+)/$', attribute.quickedit,
        name='siptrackweb.views.attribute.quickedit'),
    url(r'^attribute/quickedit/(?P<attr_name>[^/]+)/post/(?P<oid>[^/]+)/$', attribute.quickedit_post,
        name='siptrackweb.views.attribute.quickedit_post'),

    url(r'^template/apply/select/(?P<target_oid>[^/]+)/(?P<template_type>[^/]+)/$',
        template.apply_select, name='siptrackweb.views.template.apply_select'),
    url(r'^template/apply/set/(?P<target_oid>[^/]+)/(?P<template_type>[^/]+)/$', template.apply_set,
        name='siptrackweb.views.template.apply_set'),
    url(r'^template/apply/post/(?P<target_oid>[^/]+)/(?P<template_oid>[^/]+)/$',
        template.apply_post, name='siptrackweb.views.template.apply_post'),

    url(r'^template/(?P<template_type>[^/]+)/add/(?P<parent_oid>[^/]+)/$', template.add,
        name='siptrackweb.views.template.add'),
    url(r'^template/(?P<template_type>[^/]+)/add/post/(?P<parent_oid>[^/]+)/$', template.add_post,
        name='siptrackweb.views.template.add_post'),
    url(r'^template/update/(?P<oid>[^/]+)/$', template.update,
        name='siptrackweb.views.template.update'),
    url(r'^template/update/post/(?P<oid>[^/]+)/$', template.update_post,
        name='siptrackweb.views.template.update_post'),
    url(r'^template/delete/(?P<oid>[^/]+)/$', template.delete,
        name='siptrackweb.views.template.delete'),
    url(r'^template/delete/post/(?P<oid>[^/]+)/$', template.delete_post,
        name='siptrackweb.views.template.delete_post'),
    url(r'^template/rule/(?P<rule_type>[^/]+)/add/(?P<parent_oid>[^/]+)/$', template.rule_add,
        name='siptrackweb.views.template.rule_add'),
    url(r'^template/rule/(?P<rule_type>[^/]+)/add/post/(?P<parent_oid>[^/]+)/$',
        template.rule_add_post, name='siptrackweb.views.template.rule_add_post'),
    url(r'^template/rule/update/(?P<oid>[^/]+)/$', template.rule_update,
        name='siptrackweb.views.template.rule_update'),
    url(r'^template/rule/update/post/(?P<oid>[^/]+)/$', template.rule_update_post,
        name='siptrackweb.views.template.rule_update_post'),
    url(r'^template/rule/delete/(?P<oid>[^/]+)/$', template.rule_delete,
        name='siptrackweb.views.template.rule_delete'),
    url(r'^template/rule/delete/post/(?P<oid>[^/]+)/$', template.rule_delete_post,
        name='siptrackweb.views.template.rule_delete_post'),
    url(r'^template/display/(?P<oid>[^/]+)/$', template.display,
        name='siptrackweb.views.template.display'),
    url(r'^template/copy/(?P<oid>[^/]+)/$', template.copy, name='siptrackweb.views.template.copy'),
    url(r'^template/copy/post/(?P<oid>[^/]+)/$', template.copy_post,
        name='siptrackweb.views.template.copy_post'),

    url(r'^counter/(?P<parent_oid>[^/]+)/$', counter.index, name='siptrackweb.views.counter.index'),
    url(r'^counter/basic/add/(?P<parent_oid>[^/]+)/$', counter.add_basic,
        name='siptrackweb.views.counter.add_basic'),
    url(r'^counter/basic/add/post/(?P<parent_oid>[^/]+)/$', counter.add_basic_post,
        name='siptrackweb.views.counter.add_basic_post'),
    url(r'^counter/looping/add/(?P<parent_oid>[^/]+)/$', counter.add_looping,
        name='siptrackweb.views.counter.add_looping'),
    url(r'^counter/looping/add/post/(?P<parent_oid>[^/]+)/$', counter.add_looping_post,
        name='siptrackweb.views.counter.add_looping_post'),
    url(r'^counter/update/(?P<oid>[^/]+)/$', counter.update, name='siptrackweb.views.counter.update'),
    url(r'^counter/update/post/(?P<oid>[^/]+)/$', counter.update_post,
        name='siptrackweb.views.counter.update_post'),
    url(r'^counter/delete/(?P<oid>[^/]+)/$', counter.delete, name='siptrackweb.views.counter.delete'),
    url(r'^counter/delete/post/(?P<oid>[^/]+)/$', counter.delete_post,
        name='siptrackweb.views.counter.delete_post'),
    url(r'^counter/display/(?P<oid>[^/]+)/$', counter.display,
        name='siptrackweb.views.counter.display'),

    url(r'^networktree/(?P<parent_oid>[^/]+)/$', network.tree.index,
        name='siptrackweb.views.network.tree.index'),
    url(r'^networktree/add/(?P<parent_oid>[^/]+)/$', network.tree.add,
        name='siptrackweb.views.network.tree.add'),
    url(r'^networktree/add/post/(?P<parent_oid>[^/]+)/$', network.tree.add_post,
        name='siptrackweb.views.network.tree.add_post'),
    url(r'^networktree/delete/(?P<oid>[^/]+)/$', network.tree.delete,
        name='siptrackweb.views.network.tree.delete'),
    url(r'^networktree/delete/post/(?P<oid>[^/]+)/$', network.tree.delete_post,
        name='siptrackweb.views.network.tree.delete_post'),

    url(r'^network/add/(?P<parent_oid>[^/]+)/$', network.add, name='siptrackweb.views.network.add'),
    url(r'^network/add/post/(?P<parent_oid>[^/]+)/$', network.add_post,
        name='siptrackweb.views.network.add_post'),
    url(r'^network/delete/(?P<oid>[^/]+)/$', network.delete, name='siptrackweb.views.network.delete'),
    url(r'^network/delete/post/(?P<oid>[^/]+)/$', network.delete_post,
        name='siptrackweb.views.network.delete_post'),
    url(r'^network/display/(?P<oid>[^/]+)/$', network.display,
        name='siptrackweb.views.network.display'),

    url(r'^network/range/add/(?P<parent_oid>[^/]+)/$', network.range.add,
        name='siptrackweb.views.network.range.add'),
    url(r'^network/range/add/post/(?P<parent_oid>[^/]+)/$', network.range.add_post,
        name='siptrackweb.views.network.range.add_post'),
    url(r'^network/range/delete/(?P<oid>[^/]+)/$', network.range.delete,
        name='siptrackweb.views.network.range.delete'),
    url(r'^network/range/delete/post/(?P<oid>[^/]+)/$', network.range.delete_post,
        name='siptrackweb.views.network.range.delete_post'),
    url(r'^network/range/display/(?P<oid>[^/]+)/$', network.range.display,
        name='siptrackweb.views.network.range.display'),

    url(r'^device/(?P<view_oid>[^/]+)/$', device.index, name='siptrackweb.views.device.index'),
    url(r'^device/add/template/select/(?P<parent_oid>[^/]+)/$', device.add_template_select,
        name='siptrackweb.views.device.add_template_select'),
    url(r'^device/add/template/set/(?P<parent_oid>[^/]+)/$', device.add_template_set,
        name='siptrackweb.views.device.add_template_set'),
    url(r'^device/add/template/post/(?P<parent_oid>[^/]+)/(?P<template_oid>[^/]+)/$',
        device.add_template_post, name='siptrackweb.views.device.add_template_post'),
    url(r'^device/delete/(?P<oid>[^/]+)/$', device.delete, name='siptrackweb.views.device.delete'),
    url(r'^device/delete/post/(?P<oid>[^/]+)/$', device.delete_post,
        name='siptrackweb.views.device.delete_post'),
    url(r'^device/disable/(?P<oid>[^/]+)/$', device.disable, name='siptrackweb.views.device.disable'),
    url(r'^device/disable/post/(?P<oid>[^/]+)/$', device.disable_post,
        name='siptrackweb.views.device.disable_post'),
    url(r'^device/enable/(?P<oid>[^/]+)/$', device.enable, name='siptrackweb.views.device.enable'),
    url(r'^device/enable/post/(?P<oid>[^/]+)/$', device.enable_post,
        name='siptrackweb.views.device.enable_post'),
    url(r'^device/display/(?P<oid>[^/]+)/$', device.display, name='siptrackweb.views.device.display'),
    url(r'^device/export/(?P<oid>[^/]+)/$', device.export, name='siptrackweb.views.device.export'),
    url(r'^device/recreate/template/select/(?P<oid>[^/]+)/$', device.recreate_template_select,
        name='siptrackweb.views.device.recreate_template_select'),
    url(r'^device/recreate/template/set/(?P<oid>[^/]+)/$', device.recreate_template_set,
        name='siptrackweb.views.device.recreate_template_set'),
    url(r'^device/recreate/template/post/(?P<oid>[^/]+)/(?P<template_oid>[^/]+)/$',
        device.recreate_template_post, name='siptrackweb.views.device.recreate_template_post'),
    url(r'^device/copy/(?P<oid>[^/]+)/$', device.copy, name='siptrackweb.views.device.copy'),
    url(r'^device/copy/post/(?P<oid>[^/]+)/$', device.copy_post,
        name='siptrackweb.views.device.copy_post'),

    url(r'^device/category/add/(?P<parent_oid>[^/]+)/$', device.category.add,
        name='siptrackweb.views.device.category.add'),
    url(r'^device/category/add/post/(?P<parent_oid>[^/]+)/$', device.category.add_post,
        name='siptrackweb.views.device.category.add_post'),
    url(r'^device/category/delete/(?P<oid>[^/]+)/$', device.category.delete,
        name='siptrackweb.views.device.category.delete'),
    url(r'^device/category/delete/post/(?P<oid>[^/]+)/$', device.category.delete_post,
        name='siptrackweb.views.device.category.delete_post'),
    url(r'^device/category/export/(?P<oid>[^/]+)/$', device.category.export,
        name='siptrackweb.views.device.category.export'),

    url(r'^device/config/(?P<oid>[^/]+)/$', device_config.display,
        name='siptrackweb.views.device_config.display'),
    url(r'^device/config/add/(?P<parent_oid>[^/]+)/$', device_config.add,
        name='siptrackweb.views.device_config.add'),
    url(r'^device/config/add/post/(?P<parent_oid>[^/]+)/$', device_config.add_post,
        name='siptrackweb.views.device_config.add_post'),
    url(r'^device/config/delete/(?P<oid>[^/]+)/$', device_config.delete,
        name='siptrackweb.views.device_config.delete'),
    url(r'^device/config/delete/post/(?P<oid>[^/]+)/$', device_config.delete_post,
        name='siptrackweb.views.device_config.delete_post'),
    url(r'^device/config/all/(?P<oid>[^/]+)/$', device_config.display_all,
        name='siptrackweb.views.device_config.display_all'),
    url(r'^device/config/submit/(?P<oid>[^/]+)/$', device_config.submit,
        name='siptrackweb.views.device_config.submit'),
    url(r'^device/config/submit/post/(?P<oid>[^/]+)/$', device_config.submit_post,
        name='siptrackweb.views.device_config.submit_post'),
    url(r'^device/config/download/(?P<oid>[^/]+)/(?P<timestamp>[^/]+)/$', device_config.download,
        name='siptrackweb.views.device_config.download'),
    
    url(r'^device/config/template/(?P<oid>[^/]+)/$', device_config_template.display,
        name='siptrackweb.views.device_config_template.display'),
    url(r'^device/config/template/add/(?P<parent_oid>[^/]+)/$', device_config_template.add,
        name='siptrackweb.views.device_config_template.add'),
    url(r'^device/config/template/add/post/(?P<parent_oid>[^/]+)/$',
        device_config_template.add_post, name='siptrackweb.views.device_config_template.add_post'),
    url(r'^device/config/template/delete/(?P<oid>[^/]+)/$', device_config_template.delete,
        name='siptrackweb.views.device_config_template.delete'),
    url(r'^device/config/template/delete/post/(?P<oid>[^/]+)/$', device_config_template.delete_post,
        name='siptrackweb.views.device_config_template.delete_post'),
    url(r'^device/config/template/submit/(?P<oid>[^/]+)/$', device_config_template.submit,
        name='siptrackweb.views.device_config_template.submit'),
    url(r'^device/config/template/submit/post/(?P<oid>[^/]+)/$', device_config_template.submit_post,
        name='siptrackweb.views.device_config_template.submit_post'),
    url(r'^device/config/template/generate/(?P<oid>[^/]+)/$', device_config_template.generate,
        name='siptrackweb.views.device_config_template.generate'),
    url(r'^device/config/template/download/(?P<oid>[^/]+)/$', device_config_template.download,
        name='siptrackweb.views.device_config_template.download'),

    url(r'^device/network/add/(?P<oid>[^/]+)/$', device_network.add,
        name='siptrackweb.views.device_network.add'),
    url(r'^device/network/add/post/(?P<oid>[^/]+)/$', device_network.add_post,
        name='siptrackweb.views.device_network.add_post'),
    url(r'^device/network/autoassign/(?P<oid>[^/]+)/$', device_network.autoassign,
        name='siptrackweb.views.device_network.autoassign'),
    url(r'^device/network/autoassign/post/(?P<oid>[^/]+)/$', device_network.autoassign_post,
        name='siptrackweb.views.device_network.autoassign_post'),
    url(r'^device/network/delete/(?P<device_oid>[^/]+)/(?P<network_oid>[^/]+)/$',
        device_network.delete, name='siptrackweb.views.device_network.delete'),
    url(r'^device/network/delete/post/(?P<device_oid>[^/]+)/(?P<network_oid>[^/]+)/$',
        device_network.delete_post, name='siptrackweb.views.device_network.delete_post'),

    url(r'^device/(?P<type>association|reference)/delete/(?P<oid1>[^/]+)/(?P<oid2>[^/]+)/$',
        device.device_association.delete, name='siptrackweb.views.device.device_association.delete'),
    url(r'^device/(?P<type>association|reference)/delete/post/(?P<oid1>[^/]+)/(?P<oid2>[^/]+)/$',
        device.device_association.delete_post,
        name='siptrackweb.views.device.device_association.delete_post'),
    url(r'^device/association/add/(?P<oid>[^/]+)/$', device.device_association.add_with_target,
        name='siptrackweb.views.device.device_association.add_with_target'),

    url(r'^password/(?P<view_oid>[^/]+)/$', password.index, name='siptrackweb.views.password.index'),
    url(
        r'^password/display/(?P<oid>[^/]+)/$',
        password.display,
        name='siptrackweb.views.password.display'
    ),
    url(r'^password/category/add/(?P<parent_oid>[^/]+)/$', password.category_add,
        name='siptrackweb.views.password.category_add'),
    url(r'^password/category/add/post/(?P<parent_oid>[^/]+)/$', password.category_add_post,
        name='siptrackweb.views.password.category_add_post'),
    url(r'^password/category/delete/(?P<oid>[^/]+)/$', password.category_delete,
        name='siptrackweb.views.password.category_delete'),
    url(r'^password/category/delete/post/(?P<oid>[^/]+)/$', password.category_delete_post,
        name='siptrackweb.views.password.category_delete_post'),
    url(r'^password/category/display/(?P<oid>[^/]+)/$', password.category_display,
        name='siptrackweb.views.password.category_display'),
    url(r'^password/key/add/(?P<parent_oid>[^/]+)/$', password.key_add,
        name='siptrackweb.views.password.key_add'),
    url(r'^password/key/add/post/(?P<parent_oid>[^/]+)/$', password.key_add_post,
        name='siptrackweb.views.password.key_add_post'),
    url(r'^password/key/delete/(?P<oid>[^/]+)/$', password.key_delete,
        name='siptrackweb.views.password.key_delete'),
    url(r'^password/key/delete/post/(?P<oid>[^/]+)/$', password.key_delete_post,
        name='siptrackweb.views.password.key_delete_post'),
    url(r'^password/key/display/(?P<oid>[^/]+)/$', password.key_display,
        name='siptrackweb.views.password.key_display'),
    url(r'^password/add/(?P<parent_oid>[^/]+)/$', password.add,
        name='siptrackweb.views.password.add'),
    url(r'^password/add/post/(?P<parent_oid>[^/]+)/$', password.add_post,
        name='siptrackweb.views.password.add_post'),
    url(r'^password/delete/(?P<oid>[^/]+)/$', password.delete,
        name='siptrackweb.views.password.delete'),
    url(r'^password/delete/post/(?P<oid>[^/]+)/$', password.delete_post,
        name='siptrackweb.views.password.delete_post'),
    url(r'^password/update/(?P<oid>[^/]+)/$', password.update,
        name='siptrackweb.views.password.update'),
    url(r'^password/update/post/(?P<oid>[^/]+)/$', password.update_post,
        name='siptrackweb.views.password.update_post'),

    url(r'^ajax/password/key/valid/$', password.ajax_key_is_valid,
        name='siptrackweb.views.password.ajax_key_is_valid'),

    url(r'^user/$', user.index, name='siptrackweb.views.user.index'),
    url(r'^user/manager/display/(?P<oid>[^/]+)/$', user.manager_display,
        name='siptrackweb.views.user.manager_display'),
    url(r'^user/manager/add/(?P<um_type>[^/]+)/$', user.manager_add,
        name='siptrackweb.views.user.manager_add'),
    url(r'^user/manager/add/post/(?P<um_type>[^/]+)/$', user.manager_add_post,
        name='siptrackweb.views.user.manager_add_post'),
    url(r'^user/manager/update/(?P<oid>[^/]+)/$', user.manager_update,
        name='siptrackweb.views.user.manager_update'),
    url(r'^user/manager/update/post/(?P<oid>[^/]+)/$', user.manager_update_post,
        name='siptrackweb.views.user.manager_update_post'),
    url(r'^user/manager/syncusers/ldap/(?P<oid>[^/]+)/$', user.manager_ldap_syncusers,
        name='siptrackweb.views.user.manager_ldap_syncusers'),
    url(r'^user/manager/syncusers/ldap/post/(?P<oid>[^/]+)/$', user.manager_ldap_syncusers_post,
        name='siptrackweb.views.user.manager_ldap_syncusers_post'),
    url(r'^user/manager/syncusers/ad/(?P<oid>[^/]+)/$', user.manager_ad_syncusers,
        name='siptrackweb.views.user.manager_ad_syncusers'),
    url(r'^user/manager/syncusers/ad/post/(?P<oid>[^/]+)/$', user.manager_ad_syncusers_post,
        name='siptrackweb.views.user.manager_ad_syncusers_post'),
    url(r'^user/manager/activate/(?P<oid>[^/]+)/$', user.manager_activate,
        name='siptrackweb.views.user.manager_activate'),
    url(r'^user/manager/activate/post/(?P<oid>[^/]+)/$', user.manager_activate_post,
        name='siptrackweb.views.user.manager_activate_post'),
    url(r'^user/manager/delete/(?P<oid>[^/]+)/$', user.manager_delete,
        name='siptrackweb.views.user.manager_delete'),
    url(r'^user/manager/delete/post/(?P<oid>[^/]+)/$', user.manager_delete_post,
        name='siptrackweb.views.user.manager_delete_post'),
    url(r'^user/add/(?P<oid>[^/]+)/$', user.add, name='siptrackweb.views.user.add'),
    url(r'^user/add/post/(?P<oid>[^/]+)/$', user.add_post, name='siptrackweb.views.user.add_post'),
    url(r'^user/display/(?P<oid>[^/]+)/$', user.display, name='siptrackweb.views.user.display'),
    url(r'^user/delete/(?P<oid>[^/]+)/$', user.delete, name='siptrackweb.views.user.delete'),
    url(r'^user/delete/post/(?P<oid>[^/]+)/$', user.delete_post,
        name='siptrackweb.views.user.delete_post'),
    url(r'^user/password/reset/(?P<oid>[^/]+)/$', user.reset_password,
        name='siptrackweb.views.user.reset_password'),
    url(r'^user/password/reset/post/(?P<oid>[^/]+)/$', user.reset_password_post,
        name='siptrackweb.views.user.reset_password_post'),
    url(r'^user/password/update/(?P<oid>[^/]+)/$', user.update_password,
        name='siptrackweb.views.user.update_password'),
    url(r'^user/password/update/post/(?P<oid>[^/]+)/$', user.update_password_post,
        name='siptrackweb.views.user.update_password_post'),
    url(r'^user/update/(?P<oid>[^/]+)/$', user.update, name='siptrackweb.views.user.update'),
    url(r'^user/update/post/(?P<oid>[^/]+)/$', user.update_post,
        name='siptrackweb.views.user.update_post'),
    url(r'^user/connectkey/selectkey/(?P<oid>[^/]+)/$', user.connectkey_selectkey,
        name='siptrackweb.views.user.connectkey_selectkey'),
    url(r'^user/connectkey/post/(?P<oid>[^/]+)/$', user.connectkey_post,
        name='siptrackweb.views.user.connectkey_post'),
    url(r'^user/subkey/delete/(?P<oid>[^/]+)/$', user.subkey_delete,
        name='siptrackweb.views.user.subkey_delete'),
    url(r'^user/subkey/delete/post/(?P<oid>[^/]+)/$', user.subkey_delete_post,
        name='siptrackweb.views.user.subkey_delete_post'),
    url(r'^user/session/kill/(?P<session_id>[^/]+)/$', user.session_kill,
        name='siptrackweb.views.user.session_kill'),
    url(r'^user/session/kill/post/(?P<session_id>[^/]+)/$', user.session_kill_post,
        name='siptrackweb.views.user.session_kill_post'),
    url(r'^user/group/display/(?P<oid>[^/]+)/$', user.group_display,
        name='siptrackweb.views.user.group_display'),
    url(r'^user/group/add/(?P<oid>[^/]+)/$', user.group_add, name='siptrackweb.views.user.group_add'),
    url(r'^user/group/add/post/(?P<oid>[^/]+)/$', user.group_add_post,
        name='siptrackweb.views.user.group_add_post'),
    url(r'^user/group/update/(?P<oid>[^/]+)/$', user.group_update,
        name='siptrackweb.views.user.group_update'),
    url(r'^user/group/update/post/(?P<oid>[^/]+)/$', user.group_update_post,
        name='siptrackweb.views.user.group_update_post'),
    url(r'^user/group/delete/(?P<oid>[^/]+)/$', user.group_delete,
        name='siptrackweb.views.user.group_delete'),
    url(r'^user/group/delete/post/(?P<oid>[^/]+)/$', user.group_delete_post,
        name='siptrackweb.views.user.group_delete_post'),

    url(r'^ajax/user/subkey/delete/$', user.ajax_subkey_delete,
        name='siptrackweb.views.user.ajax_subkey_delete'),
    url(r'^ajax/user/connectkey/$', user.ajax_connectkey,
        name='siptrackweb.views.user.ajax_connectkey'),

    url(r'^config/add/select/(?P<parent_oid>[^/]+)/$', config.add_select,
        name='siptrackweb.views.config.add_select'),
    url(r'^config/add/set/(?P<parent_oid>[^/]+)/$', config.add_set,
        name='siptrackweb.views.config.add_set'),
    url(r'^config/add/post/(?P<parent_oid>[^/]+)/$', config.add_post,
        name='siptrackweb.views.config.add_post'),
    url(r'^config/delete/(?P<oid>[^/]+)/$', config.delete, name='siptrackweb.views.config.delete'),
    url(r'^config/delete/post/(?P<oid>[^/]+)/$', config.delete_post,
        name='siptrackweb.views.config.delete_post'),

    url(r'^permission/add/(?P<parent_oid>[^/]+)/$', permission.add,
        name='siptrackweb.views.permission.add'),
    url(r'^permission/add/post/(?P<parent_oid>[^/]+)/$', permission.add_post,
        name='siptrackweb.views.permission.add_post'),
    url(r'^permission/delete/(?P<oid>[^/]+)/$', permission.delete,
        name='siptrackweb.views.permission.delete'),
    url(r'^permission/delete/post/(?P<oid>[^/]+)/$', permission.delete_post,
        name='siptrackweb.views.permission.delete_post'),

    url(r'^command/display/(?P<oid>[^/]+)/$', command.display,
        name='siptrackweb.views.command.display'),
    url(r'^command/add/(?P<parent_oid>[^/]+)/$', command.add, name='siptrackweb.views.command.add'),
    url(r'^command/add/post/(?P<parent_oid>[^/]+)/$', command.add_post,
        name='siptrackweb.views.command.add_post'),
    url(r'^command/update/(?P<oid>[^/]+)/$', command.update, name='siptrackweb.views.command.update'),
    url(r'^command/update/post/(?P<oid>[^/]+)/$', command.update_post,
        name='siptrackweb.views.command.update_post'),
    url(r'^command/delete/(?P<oid>[^/]+)/$', command.delete, name='siptrackweb.views.command.delete'),
    url(r'^command/delete/post/(?P<oid>[^/]+)/$', command.delete_post,
        name='siptrackweb.views.command.delete_post'),

    url(r'^command/queue/display/(?P<oid>[^/]+)/$', command.queue.display,
        name='siptrackweb.views.command.queue.display'),
    url(r'^command/queue/add/(?P<parent_oid>[^/]+)/$', command.queue.add,
        name='siptrackweb.views.command.queue.add'),
    url(r'^command/queue/add/post/(?P<parent_oid>[^/]+)/$', command.queue.add_post,
        name='siptrackweb.views.command.queue.add_post'),
    url(r'^command/queue/update/(?P<oid>[^/]+)/$', command.queue.update,
        name='siptrackweb.views.command.queue.update'),
    url(r'^command/queue/update/post/(?P<oid>[^/]+)/$', command.queue.update_post,
        name='siptrackweb.views.command.queue.update_post'),
    url(r'^command/queue/delete/(?P<oid>[^/]+)/$', command.queue.delete,
        name='siptrackweb.views.command.queue.delete'),
    url(r'^command/queue/delete/post/(?P<oid>[^/]+)/$', command.queue.delete_post,
        name='siptrackweb.views.command.queue.delete_post'),

    url(r'^event/trigger/display/(?P<oid>[^/]+)/$', event.trigger.display,
        name='siptrackweb.views.event.trigger.display'),
    url(r'^event/trigger/add/(?P<parent_oid>[^/]+)/$', event.trigger.add,
        name='siptrackweb.views.event.trigger.add'),
    url(r'^event/trigger/add/post/(?P<parent_oid>[^/]+)/$', event.trigger.add_post,
        name='siptrackweb.views.event.trigger.add_post'),
    url(r'^event/trigger/update/(?P<oid>[^/]+)/$', event.trigger.update,
        name='siptrackweb.views.event.trigger.update'),
    url(r'^event/trigger/update/post/(?P<oid>[^/]+)/$', event.trigger.update_post,
        name='siptrackweb.views.event.trigger.update_post'),
    url(r'^event/trigger/delete/(?P<oid>[^/]+)/$', event.trigger.delete,
        name='siptrackweb.views.event.trigger.delete'),
    url(r'^event/trigger/delete/post/(?P<oid>[^/]+)/$', event.trigger.delete_post,
        name='siptrackweb.views.event.trigger.delete_post'),

    url(r'^event/trigger/rule/python/display/(?P<oid>[^/]+)/$', event.trigger_rule_python.display,
        name='siptrackweb.views.event.trigger_rule_python.display'),
    url(r'^event/trigger/rule/python/add/(?P<parent_oid>[^/]+)/$', event.trigger_rule_python.add,
        name='siptrackweb.views.event.trigger_rule_python.add'),
    url(r'^event/trigger/rule/python/add/post/(?P<parent_oid>[^/]+)/$',
        event.trigger_rule_python.add_post,
        name='siptrackweb.views.event.trigger_rule_python.add_post'),
    url(r'^event/trigger/rule/python/update/(?P<oid>[^/]+)/$', event.trigger_rule_python.update,
        name='siptrackweb.views.event.trigger_rule_python.update'),
    url(r'^event/trigger/rule/python/update/post/(?P<oid>[^/]+)/$',
        event.trigger_rule_python.update_post,
        name='siptrackweb.views.event.trigger_rule_python.update_post'),
    url(r'^event/trigger/rule/python/delete/(?P<oid>[^/]+)/$', event.trigger_rule_python.delete,
        name='siptrackweb.views.event.trigger_rule_python.delete'),
    url(r'^event/trigger/rule/python/delete/post/(?P<oid>[^/]+)/$',
        event.trigger_rule_python.delete_post,
        name='siptrackweb.views.event.trigger_rule_python.delete_post'),

    url(r'^rack/unit/reserved/(?P<device_oid>[^/]+)/$', device.rack_unit_reserved,
        name='siptrackweb.views.device.rack_unit_reserved'),
    url(r'^rack/unit/reserved/post/(?P<device_oid>[^/]+)/$', device.rack_unit_reserved_post,
        name='siptrackweb.views.device.rack_unit_reserved_post'),
    url(r'^rack/unit/unreserved/(?P<device_oid>[^/]+)/$', device.rack_unit_unreserved,
        name='siptrackweb.views.device.rack_unit_unreserved'),

    url(r'^rack/unit/occupied/(?P<device_oid>[^/]+)/$', device.rack_unit_occupied,
        name='siptrackweb.views.device.rack_unit_occupied'),
    url(r'^rack/unit/occupied/post/(?P<device_oid>[^/]+)/$', device.rack_unit_occupied_post,
        name='siptrackweb.views.device.rack_unit_occupied_post'),
    url(r'^rack/unit/unoccupied/(?P<device_oid>[^/]+)/$', device.rack_unit_unoccupied,
        name='siptrackweb.views.device.rack_unit_unoccupied'),

    url(r'^tag/(?P<oid>[^/]+)/$', root.tag_oid, name='siptrackweb.views.root.tag_oid'),
    url(r'^untag/(?P<oid>[^/]+)/$', root.untag_oid, name='siptrackweb.views.root.untag_oid'),
    url(r'^relocate/tagged/(?P<oid>[^/]+)/$', root.relocate_tagged_oid,
        name='siptrackweb.views.root.relocate_tagged_oid'),
    url(r'^toggle-verbose/(?P<oid>.*)/$', root.toggle_verbose,
        name='siptrackweb.views.root.toggle_verbose'),
    url(r'^search/$', root.search, name='siptrackweb.views.root.search'),
    url(r'^login/$', root.login, name='siptrackweb.views.root.login'),
    url(r'^logout/$', root.logout, name='siptrackweb.views.root.logout'),
    url(r'^dinfo/$', root.dinfo, name='siptrackweb.views.root.dinfo'),
    url(r'^style.css$', root.style, name='siptrackweb.views.root.style'),
    url(r'^prototype.js$', root.prototypejs, name='siptrackweb.views.root.prototypejs'),
]

